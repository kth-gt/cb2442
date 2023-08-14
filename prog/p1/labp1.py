
# LAB P1

# This file contains the code for the first lab assignment.
# Please read the assignment carefully and implement the functions blank function.
# You can run the code by typing "python labp1.py" in the terminal.
# A more advanced test suite is available by executing "python runner.py".

# This list contains the names of the authors of this program. 
# Please change the names to your names.

authors = ['A. Student', 'B. Helper']


# A dictionary converting codons to amino acids

codon2aa = {
    'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAT': 'N',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGT': 'S',
    'ATA': 'I', 'ATC': 'I', 'ATG': 'M', 'ATT': 'I',
    'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAT': 'H',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAT': 'D',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'TAA': '*', 'TAC': 'Y', 'TAG': '*', 'TAT': 'Y',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TGA': '*', 'TGC': 'C', 'TGG': 'W', 'TGT': 'C',
    'TTA': 'L', 'TTC': 'F', 'TTG': 'L', 'TTT': 'F'
}


# Edit this function to return the amino acid sequence of a provided DNA sequence
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
# This is not a manitory part of the assignment, 
# but it is a nice excercise if the students have extra time
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


# Here is a function that reads a FASTA file and returns strings containing tupples of (sequence name, sequence)
# In our case the sequences will be a DNA sequences
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

# Here is a function that reads a DNA FASTA and writes a protein FASTA
# It uses the functions above, and hence sdepends on your implementation 
# of dna2aa()
def dna2aa_fasta(dna_filename, protein_filename):
    seqs = read_fasta(dna_filename)
    protein_seqs = []
    for name, seq in seqs:
        protein_seqs.append((name, dna2aa(seq)))
    write_fasta(protein_filename, protein_seqs)


# Test code for the dna2aa function. 
# Will only be executed if this file is run directly e.g. with "python labp1.py"
if __name__ == "__main__":
    dna2aa("ATGATGATG")
    dna2aa_fasta('cdna.faa', 'output.faa')

