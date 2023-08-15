#! /bin/env python
# -*- coding: utf-8 -*-

import filecmp
import labp1 as lab

# This is a test suite for the first lab assignment.
# It is executed by running "python runner.py" in the terminal.
def runner():
    assert lab.dna2aa('ATTGCGATGGCGCCGGAACCGACCATTGATGAATAA') == 'IAMAPEPTIDE*'
    assert lab.dna2aa('ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA') == 'MAMAPRTEINSTRING*'
    lab.dna2aa_fasta('cdna.faa', 'output.faa')
    assert filecmp.cmp('output.faa', '0shift.faa', shallow=False) == True
    for author in lab.authors:
        print(author)
    print('made a function that passed all tests!')


if __name__ == "__main__":
    runner()