# Programming Lab P1

This is an introductory lab for the programming part of the course.
Your task is to write a function that can convert mRNA sequence to amino acid sequence.
To your help you have a scaffold of python code that you should use as to validate your code and also to make sure you follow a standard that the TAs can automatically validate.

### Installation

Begin with downloading the project to your local computer by using this [link](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fkth-gt%2Fcb2442%2Ftree%2Fmain%2Fprog%2Fp1). 


Unzip the files into a directory and open the directory in VScode. 
```bash
$ unzip 'kth-gt cb2442 main prog-p1.zip'
$ code .
```

### Implementation

Add a python function to the file `labp1.py` named

```python
def dna2aa(dna_str):
```

that takes a dna sequence as input and returns an amino acid sequence. You may use the dictionary `codon2aa`. which translates tripplets of bases into amino acid symbols.
Also, set the list authors to contain all the group members names.  

### Test

You can make an initial execution of your `dna2aa` function by running the ain function of the python file itself by executing the line,

```bash
$ python3 labp1.py
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

### Extra excercise

Change the behaviour of `dna2aa` so that it tries all thre possible frames of translation, and selects the amino acid sequence that has the longest orf of the three alternatives.