import filecmp
import numpy as np
import labp4 as lab

# This is a test suite for labp4.
# It is executed by running "python3 runnerp4.py" in the terminal.
def runner():
    dist_matr = np.array([[0, 0.1, 0.2, 0.3],
                          [0.1, 0, 0.2, 0.3],
                          [0.2, 0.2, 0, 0.3],
                          [0.3, 0.3, 0.3, 0]])
    names_list = ['S1', 'S2', 'S3', 'S4']
    nwk = lab.upgma(dist_matr,names_list)
    print('Tree 1:', nwk)
    ok = 0 
    if (nwk == '(S4,(S3,(S1,S2)));'):
        ok = 1
    if (nwk == '(S4,((S1,S2),S3));'):
        ok = 1
    if (nwk == '(((S1,S2),S3),S4);'):
        ok = 1
    if (nwk == '(S4,(S3,(S2,S1)));'):
        ok = 1
    if (nwk == '(S4,((S2,S1),S3));'):
        ok = 1
    if (nwk == '(((S2,S1),S3),S4);'):
        ok = 1
    assert ok == 1, f"Unexpected tree topology or tree format  for Tree 1: "+nwk

    dist_matr = np.array([[0, 0.2, 0.3, 0.4, 0.4],
                          [0.2, 0, 0.3, 0.4, 0.4],
                          [0.3, 0.3, 0, 0.35, 0.1],
                          [0.4, 0.4, 0.35, 0, 0.45],
                          [0.4, 0.4, 0.1, 0.45, 0]])
    names_list = ['S1', 'S2', 'S3', 'S4', 'S5']
    nwk = lab.upgma(dist_matr,names_list)
    print('Tree 2:', nwk)
    ok = 0 
    if (nwk == '(S4,((S3,S5),(S1,S2)));'):
        ok = 1
    if (nwk == '(S4,((S5,S3),(S1,S2)));'):
        ok = 1
    if (nwk == '(S4,((S3,S5),(S2,S1)));'):
        ok = 1
    if (nwk == '(S4,((S5,S3),(S2,S1)));'):
        ok = 1

    if (nwk == '(S4,((S1,S2),(S3,S5)));'):
        ok = 1
    if (nwk == '(S4,((S2,S1),(S3,S5)));'):
        ok = 1
    if (nwk == '(S4,((S1,S2),(S5,S3)));'):
        ok = 1
    if (nwk == '(S4,((S2,S1),(S5,S3)));'):
        ok = 1
    
    if (nwk == '(((S3,S5),(S1,S2)),S4);'):
        ok = 1
    if (nwk == '(((S5,S3),(S1,S2)),S4);'):
        ok = 1
    if (nwk == '(((S3,S5),(S2,S1)),S4);'):
        ok = 1
    if (nwk == '(((S5,S3),(S2,S1)),S4);'):
        ok = 1

    if (nwk == '(((S1,S2),(S3,S5)),S4);'):
        ok = 1
    if (nwk == '(((S2,S1),(S3,S5)),S4);'):
        ok = 1
    if (nwk == '(((S1,S2),(S5,S3)),S4);'):
        ok = 1
    if (nwk == '(((S2,S1),(S5,S3)),S4);'):
        ok = 1
    assert ok == 1, f"Unexpected tree topology or tree format for Tree 2: "+nwk

    for author in lab.authors:
        print(author)
    print('made a function that passed all tests!')

if __name__ == "__main__":
    runner()
