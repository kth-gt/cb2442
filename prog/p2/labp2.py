
import numpy as np
authors = ['A. Student', 'B. Helper']

# Initiating dynamic programming matrices, S and trace
def initiate_global_dp(m,n):
    S = np.zeros((m,n))       # An m*n matrix, initiated with 0's
    trace = np.zeros((m,n,2)) # An m*n matrix, initiated with (0,0)'s
    S[0,0] = 0.
    trace[0,0,:] = (0.,0.)
    for i in range(1,m):
        S[i,0] = i * gap_penalty()
        trace[i,0,:] =(-1,0)
    for j in range(1,n):
        S[0,j] = j * gap_penalty()
        trace[0,j,:] =(0,-1)
    return S,trace

def global_align(seqA,seqB,print_dynamic_matrix = False):
    # Initiating variables
    m, n = len(seqA)+1, len(seqB)+1
    S,trace = initiate_global_dp(m,n)
    # Fill in the rest of the dynamic programming matrix
    for i in range(1,m):
        for j in range(1,n):
            # Note the subtraction of 1 for the sequence position
            # In python sequences are indexed from 0 to len-1
            match = S[i-1,j-1] + match_score(seqA[i-1],seqB[j-1]) 
            delete = S[i-1,j] + match_score(seqA[i-1],'-') 
            insert = S[i,j-1] + match_score('-',seqB[j-1]) 
            S[i,j] = max(match,delete,insert)
            if match >= max(insert,delete):
                trace[i,j,:] = (-1,-1)
            elif delete >= insert:
                trace[i,j,:] = (-1,0)
            else:
                trace[i,j,:] = (0,-1)
    if print_dynamic_matrix:
        print_dynamic(seqA,seqB,S)
    return S, S[-1,-1]

def gap_penalty():
    return -2.0


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
    print('{:^5}'.format(" "), end=""),
    for j in range(n):
        print('{:^5}'.format(seqB[j]), end="")
    print()
    for i in range(m):
        print ('{:^5}'.format(seqA[i]), end="")
        for j in range(n):
            print ('{:5.1f}'.format(dpm[i,j]), end="")
        print()
    print()

# Format an alignment by inserting gaps in sequences
def format_alignment(seqA,seqB,S,trace):
    print("Best score: " + str(S[-1,-1]))
    outA,outB = "",""
    i,j = len(seqA),len(seqB)
    while i>0 or j>0:
        di,dj = trace[i,j]
        i += int(di)
        j += int(dj)
        if di == 0:
            outA = "-" + outA
        else:
            outA = seqA[i] + outA
        if dj == 0:
            outB = "-" + outB
        else:
            outB = seqB[j] + outB
    return outA,outB







## Here is an example implementation of a function that translates
# an RNA string into a protein string
def dna2aa(dna_str):
    aa_str = ''
    for i in range(0, len(dna_str), 3):
        codon = dna_str[i:i+3]
        if codon not in codon2aa:
            continue
        aa = codon2aa[codon]
        aa_str += aa
    return aa_str

## Here is an example implementation of an extended function that
# handles three frames and returns the longest ORF
def dna2aa_3frame(dna_str):
    aa_str, longest_orf = '', 0
    for frame in range(0, 3):
        frame_longest_orf, frame_aa_str = 0, ''
        len_orf = 0
        for i in range(frame, len(dna_str), 3):
            codon = dna_str[i:i+3]
            if codon not in codon2aa:
                continue
            aa = codon2aa[codon]
            if aa == '*':
                if len_orf > longest_orf:
                    frame_longest_orf = len_orf
                    len_orf = 0
                else:
                    len_orf += 1
            frame_aa_str += aa
        if frame_longest_orf > longest_orf:
            longest_orf = frame_longest_orf
            aa_str = frame_aa_str
    return aa_str


## Here is a function that reads a FASTA file and returns strings containing tupples of (sequence name, sequence)
def read_fasta(filename):
    seqs = []
    with open(filename) as f:
        name = None
        seq = ''
        for line in f:
            if line[0] == '>':
                if name is not None:
                    seqs.append((name, seq))
                name = line[1:].strip()
                seq = ''
            else:
                seq += line.strip()
        seqs.append((name, seq))
    return seqs

## Here is a function that writes a FASTA file from a list of (sequence name, sequence) tuples
def write_fasta(filename, seqs):
    with open(filename, 'w') as f:
        for name, seq in seqs:
            f.write('>' + name + '\n')
            f.write(seq + '\n')

## Here is a function that reads a RNA FASTA and writes a protein FASTA
def dna2aa_fasta(dna_filename, protein_filename):
    seqs = read_fasta(dna_filename)
    protein_seqs = []
    for name, seq in seqs:
        protein_seqs.append((name, dna2aa(seq)))
    write_fasta(protein_filename, protein_seqs)


# Test code for the dna2aa function. 
# Will only be executed if this file is run directly
if __name__ == "__main__":
    dna2aa("ATGATGATG")
    dna2aa_fasta('cdna.faa', 'output.faa')

