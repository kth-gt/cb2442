# Programming Lab P2 - Pairwise alignments

Your task is to write a function that can align two sequences. 
### Installation

Begin with downloading the project to your local computer by using this [link](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fkth-gt%2Fcb2442%2Ftree%2Fmain%2Fprog%2Fp2). 


Unzip the files into a directory and open the directory in VScode. 
```bash
$ unzip 'kth-gt cb2442 main prog-p2.zip'
$ code .
```

### Implementation

#### Initiation

Set the list `authors` to contain all the group members names.  

Add a python function to the file `labp2.py` named

```python
def initiate(len_str_a, len_str_b):
```

that takes the length of two sequences, `a` and `b`, as input, and outpus a (dynamic programming) matrix of dimentions `[len_str_a,len_str_b]` initiated to perform a Needleman-Wunsch global alignment. To your aid, you have the function `gap()` that returns the penalty of a gap of one amino acid.


### Test

You can make an initial execution of your `dna2aa` function by running the ain function of the python file itself by executing the line,

```bash
$ python3 labp2.py
```

However ther final test of the code is done by executing the `runner.py` executable, which can be exected from command line as, 

```bash
$ python3 runner.py
```

or just

```bash
$ ./runner.py
```

This executes the code in `labp1.py`, and validates the results against some known test vectors.
If you implemented the function right, you will see your names apearing.

### Extra excercises

If you have extra time, you can try out one or more of the following excercises:

1. Reimplement the two functions, so that they take an extra boolean argument `global` indicating if you want a global or local alignment and add the extra code for making a local alignment.
2. Reimplement the program so that it can handle affine gaps, i.e. that there is a higher penalty associated with opening than extending a gap. For that to work you will need to use three different matrices, 1 for match/missmatches, and 2 for keeping track of possible extensions of penalties in each of the sequences. A detailed description can be found e.g. [here](https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/gaps.pdf).
