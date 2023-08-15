#!/usr/bin/env python

# Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ====== CHANGES GO HERE =============
FILE = "DEA.txt"  # Your DEA file
FDR = 0.1         # Your FDR threshold
# ====================================

# Read input file
dea_results = pd.read_table(FILE, sep="\t", header=0)

# Remove inf
dea_results = dea_results.replace([np.inf, -np.inf], np.nan)
dea_results = dea_results.dropna(subset=["log2(fold_change)"], how="all")

# Extract significant entries
significant = dea_results["q_value"] <= FDR

# Colour significant points red
colors = np.where(significant, "red", "blue")

# Volcano plot
fig, a = plt.subplots(figsize=(30, 30))
x_points = dea_results["log2(fold_change)"]
y_points = -np.log10(dea_results["p_value"])
x_points_conf = dea_results[dea_results["q_value"] <= FDR]["log2(fold_change)"]
y_points_conf = -np.log10(dea_results[dea_results["q_value"] <= FDR]["p_value"])
OFFSET = 0.1
a.set_xlim([min(x_points) - OFFSET, max(x_points) + OFFSET])
a.set_ylim([min(y_points) - OFFSET, max(y_points) + OFFSET])
a.set_xlabel("Log2 Fold Change")
a.set_ylabel("-log10(p-value)")
a.set_title("Volcano plot", size=10)
a.scatter(x_points, y_points, c=colors, edgecolor="none")
a.vlines(0, 0, max(y_points), linestyles='dashed')
for gene, x, y in (
    xs for s, *xs in zip(significant, dea_results["gene"], x_points, y_points) if s
):
    a.annotate(gene, (x, y))

# Save figure
fig.savefig("volcano.pdf", dpi=300)
