# Alignments Module

Welcome to the Alignments module!

The module is composed of 5 in-class activities (L2–L5, L7), of which the four later require preparations.

All preparatory reading is in the course book, [Bioinformatics for Biotechnology Students](https://www.kaell.se/bibook). It is a living document — if you find an error, please report it with the "suggest an edit" or "open an issue" buttons in the book's top bar.

## At L2 (in class)

* [Slides: Introduction to alignments](intro/align.html)

## Before L3

Read the following chapters of the book:

* Chapter 3: [Needleman-Wunsch Algorithm: Global Alignment](https://www.kaell.se/bibook/pairwise/needleman), with code in [chapter 4](https://www.kaell.se/bibook/pairwise/nw-code)
* Chapter 5: [Smith-Waterman Algorithm: Local Alignment](https://www.kaell.se/bibook/pairwise/waterman), with code in [chapter 6](https://www.kaell.se/bibook/pairwise/sw-code)
* Chapter 7: [Semi-global Alignment](https://www.kaell.se/bibook/pairwise/semi), with code in [chapter 8](https://www.kaell.se/bibook/pairwise/sg-code)

## At L3 (in class)

* We will start with a quiz on the content of the preparatory material (see course PM about bonus points)
* We will work through the dynamic programming matrix by hand, and go through the notebook [pairwise.ipynb](code/pairwise.ipynb)

## Before L4

Read the following chapter of the book:

* Chapter 9: [Aligning Proteins](https://www.kaell.se/bibook/protein/matrix), with code in [chapter 10](https://www.kaell.se/bibook/protein/prot-code)

Read Eddy, S.R. [Where did the BLOSUM62 alignment score matrix come from?](https://doi.org/10.1038/nbt0804-1035) Nat Biotechnol 22, 1035–1036 (2004)

## At L4 (in class)

* We will start with a quiz on the content of the preparatory material (see course PM about bonus points)

## Before L5

Read the following chapters of the book:

* Chapter 11: [Multiple Sequence Alignments](https://www.kaell.se/bibook/msa/progressive), with code in [chapter 12](https://www.kaell.se/bibook/msa/msa)
* Chapter 13: [Sequence Logos](https://www.kaell.se/bibook/msa/seqlogo)
* Chapter 14: [Profile Hidden Markov Models](https://www.kaell.se/bibook/msa/profilehmm), with code in [chapter 15](https://www.kaell.se/bibook/msa/viterbi)

## At L5 (in class)

* We will start with a quiz on the content of the preparatory material (see course PM about bonus points)
* We will go through the notebook [msa.ipynb](code/msa.ipynb)

## Before L7

Read the following chapter of the book:

* Chapter 16: [The BLAST Algorithm for Sequence Retrieval](https://www.kaell.se/bibook/retrieval/blast), with code in [chapter 17](https://www.kaell.se/bibook/retrieval/blast-code)

Try to BLAST a sequence yourself — enter e.g. "APEPTIDETHATILIKE", or your own name, into [NCBI's BLAST webserver](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch)

## At L7 (in class)

* We will start with a quiz on the content of the preparatory material (see course PM about bonus points)

## Additional recommended reading

* Eddy, S.R. [What is dynamic programming?](https://doi.org/10.1038/nbt0704-909) Nat Biotechnol 22, 909–910 (2004)
* Altschul, S.F. et al. [Basic local alignment search tool.](https://doi.org/10.1016/S0022-2836%2805%2980360-2) J Mol Biol 215, 403–410 (1990) — the original BLAST paper
* Durbin, R. et al. Biological Sequence Analysis, Cambridge University Press (1998), chapters 2–6 — a deeper treatment of dynamic programming alignment and profile HMMs
