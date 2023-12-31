# Programming Lab P2 - Pairwise alignments

Your task is to write a function that can align two sequences using the Needleman-Wunch algorithm for global sequence alignment.

## Preparations

### Installation

Begin with downloading the project to your local computer by using this [link](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fkth-gt%2Fcb2442%2Ftree%2Fmain%2Fprog%2Fp2). 


Unzip the files into a directory and open the directory in VScode. 
```bash
$ unzip 'kth-gt cb2442 main prog-p2.zip'
$ code .
```

## Implementation

### Initiation

Set the list `authors` to contain all the group members names.  

Add a python function to the file `labp2.py` named

```python
def initiate_global_dp(len_str_a, len_str_b):
```

that takes the length of two sequences, `a` and `b`, as input, and outpus a (dynamic programming) matrix of dimentions `[len_str_a,len_str_b]` as well as a tracer matrix, both initiated to perform a Needleman-Wunsch global alignment. 
To your aid, you have the function `gap()` that returns the penalty of a gap of one amino acid.
Remember that in a Needleman-Wunch Algorithm, we initiate the dynamic programming matrix, $S$, is initiated as:

$$S_{i0}=g \cdot i, \forall i,$$

$$S_{0j}=g \cdot j, \forall j.$$

Furthermore the trace matrix should be initited in such a way that the alignment, once it reaches the first colum or row, goes back to (0,0), i.e. if you follow the suggested notation of the module, you should set trace(x,y,1) = True for first column, and trace(x,y,2) = True for first row (except for 0,0)

The function `initiate_global_dp` should return a tuple with the dynamic programming matrix and the trace matrix.

### Recursion

Now implement the function

```python
def global_align(seqA,seqB):
```

that fills in the rest of the dynamic programming matrix using the recursion:

$$
S_{ij} = \max \left\{ \begin{array}{ll}
S_{i-1,j-1} & +d(a_i,b_j)\\
S_{i-1,j} & +d(a_i,-)\\
S_{i,j-1} & +d(-,b_j)
\end{array}\right.
$$

Also, fill in the trace matrix, so that it follows the maximal paths through the matrix. I.e. set the trace to be

* trace(x,y,0) indicates a match in x,y
* trace(x,y,1) indicates an insert in x,y (fix column)
* trace(x,y,2) indicates a delete in x,y (fix row)

The function should return the dynamic programming matrix, the trace matrix, and the score of the alignment

### Test

You can make an initial execution of your `dna2aa` function by running the ain function of the python file itself by executing the line,

```bash
$ python labp2.py
```

However ther final test of the code is done by executing the `runnerp2.py` executable, which can be exected from command line as,

```bash
$ python runnerp2.py
```

or just

```bash
$ ./runnerp2.py
```

This executes the code in `labp2.py`, and validates the results against some known test vectors.
If you implemented the function right, you will see your names apearing.

### Extra excercises

If you have extra time, you can try out one or more of the following excercises:

1. Reimplement the two functions, so that they take an extra boolean argument `global` indicating if you want a global or local alignment and add the extra code for making a local alignment.
2. Reimplement the program so that it can handle affine gaps, i.e. that there is a higher penalty associated with opening than extending a gap. For that to work you will need to use three different matrices, 1 for match/missmatches, and 2 for keeping track of possible extensions of penalties in each of the sequences. A detailed description can be found e.g. [here](https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/gaps.pdf).
