#! /bin/env python
# -*- coding: utf-8 -*-

import numpy as np
# Replace these names with your names
authors = ['A. Student', 'B. Helper']

# Initiating dynamic programming matrices, S and trace,
# Input is the lengths of each of the two sequences
# Output is the initiated dynamic programing and trace matrices
def initiate_global_dp(m,n):
    S = np.zeros((m+1, n+1))       # An (m+1)*(n+1) matrix, initiated with 0's
    # For the trace matrix we use a three dimentional matrix of booleans
    # where 
    #   trace(x,y,0) indicates a match in x,y
    #   trace(x,y,1) indicates an insert in x,y (fix column)
    #   trace(x,y,2) indicates a delete in x,y (fix row)
    trace = np.zeros((m+1, n+1, 3), dtype=np.bool8) # An (m+1)*(n+1)*3 boolean matrix, initiated with (False,False,False)
    # First initiate the origin (0,0) here:

    # Now, fill in the first row and the first column of the matrix
    # Initiate the first column of S and trace here:

    # Initiate the first row of S and trace here:

    # Return the initiated matrices
    return S, trace

# Fill in the dynamic programming matrix and the trace
def global_align(seqA,seqB):
    # Initiating variables
    m, n = len(seqA), len(seqB)
    S,trace = initiate_global_dp(m,n)
    # Fill in the rest of the dynamic programming matrix, and the trace

    return S, trace, score_of_the_alignment

## The following functioins are give to you as a help
# Return the gap penalty
def gap_penalty():
    return -2.0

# Return the match score of letterA and letterB.
# If one of the letters is a gap, return the gap penalty
# otherwise return their match/mismatch score
def match_score(letterA,letterB):
    if letterA == '-' or letterB == '-':
        return gap_penalty()
    elif letterA == letterB:
        return 3.0
    else:
        return -1.0
    
# Print 2 sequences on top of each other
def print_alignment(seqA,seqB):
    print(seqA)
    print(seqB)

# Print a dynamic programming score matrix
# together with its sequences
def print_dynamic(seqA,seqB,dpm):
    seqA,seqB = "-" + seqA, "-" + seqB
    m,n = len(seqA),len(seqB)
    print('{:^5}'.format(' '), end=''),
    for j in range(n):
        print('{:^5}'.format(seqB[j]), end='')
    print()
    for i in range(m):
        print ('{:^5}'.format(seqA[i]), end="")
        for j in range(n):
            print ('{:5.1f}'.format(dpm[i,j]), end="")
        print()
    print()

# Format an alignment by inserting gaps in sequences given a trace matrix
def format_alignment(seqA, seqB, trace, start_from = None):
    if start_from:
        i, j = start_from
    else:
        i, j = len(seqA), len(seqB)
    outA, outB = "",""
    while i>0 or j>0:
        if trace[i,j,0]: # match
            i, j = i-1, j-1
            outA = seqA[i] + outA
            outB = seqB[j] + outB
        elif trace[i,j,1]: # insert
            i, j = i, j-1
            outA = "-" + outA
            outB = seqB[j] + outB
        elif trace[i,j,2]: # delete
            i, j = i-1, j
            outA = seqA[i] + outA
            outB = "-" + outB
    return outA,outB



# Test code for the dna2aa function. 
# Will only be executed if this file is run directly
# e.g. by running the command "python labp2.py"
if __name__ == "__main__":
    seqA, seqB = "ATG", "GAT"
    dp, trace, max_score = global_align(seqA, seqB)
    print_dynamic(seqA, seqB, dp)
    print('\n'.join(format_alignment(seqA, seqB, trace)))
    print(f"Score: {max_score}")
