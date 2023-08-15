#! /bin/env python3
import labp2 as lab

# This is a test suite for the first lab assignment.
# It is executed by running "python runner.py" in the terminal.
def runner():
    S, trace, score = lab.global_align("GATTA","GCTAC")
    assert score == 4.0

    S, trace, score = lab.global_align("CTATCTCGCTATCCA","CTACGCTATTTCA")
    assert score == 24.0

    for author in lab.authors:
        print(author)
    print('made a function that passed all tests!')

if __name__ == "__main__":
    runner()