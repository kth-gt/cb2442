#! /bin/env python3
import labp2 as lab

def runner():
    S, score = lab.global_align("GATTA","GCTAC",True)
    assert score == 4.0

    S, score = lab.global_align("CTATCTCGCTATCCA","CTACGCTATTTCA",True)
    assert score == 24.0

    for author in lab.authors:
        print(author)
    print('made a function that passed all tests!')


if __name__ == "__main__":
    runner()