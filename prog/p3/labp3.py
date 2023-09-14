import sys
import matplotlib.pyplot as plt
import numpy as np

# Replace these names with your names
authors = ['A. Student', 'B. Helper']

# Input arguments
annotfile = sys.argv[1]
countfile = sys.argv[2]

# Function that returns true if a key is present in a dictionary, otherwise returns false
def is_key_present(dictionary, key):
    return key in dictionary

# Dictionaries for storing read counts and gene lengths
gene_length = {}
readcount = {}

# Dictionaries for storing rpkm and tpm values
rpkm = {}
tpm = {}

# Your implementation starts here. Add the appropriate code to solve the tasks.

# Read input files
## use dictionaries to store the read counts and gene lengths

# Task #1: Calculate RPKM and TPM, print the values for all genes in the annotfile print to STDOUT
## implement the RPKM and TPM algorithms, and store the values in dictionaries

# Task #2: Plot TPM vs. RPKM in a scatterplot
## use plt.scatter() from matplotlib to create the plot and plt.savefig() to save the plot as a png file



