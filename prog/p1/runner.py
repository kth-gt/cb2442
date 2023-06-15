#! /bin/env python3
import filecmp
import labp1 as lab

def runner():
    assert lab.dna2aa('ATTGCGATGGCGCCGGAACCGACCATTGATGAATAA') == 'IAMAPEPTIDE*'
    assert lab.dna2aa('ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA') == 'MAMAPRTEINSTRING*'
    lab.dna2aa_fasta('cdna.faa', 'output.faa')
    assert filecmp.cmp('output.faa', 'desired.faa', shallow=False) == True
    for author in lab.authors:
        print(author)
    print('made a function that passed all tests!')


if __name__ == "__main__":
    runner()