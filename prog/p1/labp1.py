# A dictionary converting codons to amino acids

authors = ['A. Student', 'B. Helper']

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

## Here is a function that translates an RNA string into a protein string
def dna2aa(dna_str):
    aa_str = ''
    for i in range(0, len(dna_str), 3):
        codon = dna_str[i:i+3]
        if len(codon) == 3:
            aa = codon2aa[codon]
            aa_str += aa
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
