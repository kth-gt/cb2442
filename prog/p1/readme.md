# Programming Lab P1

This is an introductory lab for the programming part of the course.
Your task is to write a function that can convert mRNA sequence to amino acid sequence.
To your help you have a scaffold of python code that you should use as to validate your code and also to make sure you follow a standard that the TAs can automatically validate.

### Implementation

Add a python function to the file labp1.py named

```python
def dna2aa(dna_str):
```

that takes a dna sequence as input and returns an amino acid sequence. You may use the dictionary `codon2aa`. which translates tripplets of bases into amino acid symbols.
Also, set the list authors to contain all the group members names.  

### Test

The code should be tested using the `runner.py` executable, which can be exected from command line as 

```bash
$ ./runner.py
```

This executes the code in `labp1.py`, and validates the results against some known test vectors.
If you implemented the function right, you will see your names apearing.
