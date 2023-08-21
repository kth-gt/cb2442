# Programming Lab P1

This is an introductory lab for the programming part of the course. Your task is to write a function that can convert DNA sequence to amino acid sequence. To your help you have a scaffold of python code that you should use as to validate your code and also to make sure you follow a standard that the TAs can automatically validate.

### Code Installation

Begin with downloading the project to your local computer by using this [link](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fkth-gt%2Fcb2442%2Ftree%2Fmain%2Fprog%2Fp1).

Unzip the files into a directory and open the directory in VS Code.

```bash
$ unzip 'kth-gt cb2442 main prog-p1.zip'
$ code .
```

### VSCode

If you are not yet familiar with the VS Code software, watch for example this [short introduction video](https://code.visualstudio.com/docs/introvideos/basics). Note that you can run your code directly in VS Code and don't need to open a separate terminal window. You can run either the whole script by e.g. pressing the start symbol in the upper right corner or by typing `labp1.py` in the terminal window below the code window (if you don't see it, select "Terminal" in the "View" menu). You can also run Python in interactive mode by typing `python3` in the terminal window. This will give you a `>>>` prompt and now you can paste (or type) sections of the code that will be executed. Another way to do this is to mark a section of the code, right-click, and select "Run Python" / "Run Selection/Line in Python Terminal" (or press Shift+Enter). Don't forget to save every now and then.

### Implementation

In the Python script file `labp1.py`, edit the function named

```python
def dna2aa(dna_str):
```

so that it takes a DNA sequence as input and returns an amino acid sequence. You may use the dictionary `codon2aa`. which translates triplets of bases into amino acid symbols.
Also, set the list `authors` to contain all the group members' names.  

### Test

You can make an initial execution of your `dna2aa` function by running the Python file itself directly as top-level code by executing the line,

```bash
$ python labp1.py
```

However the final test of the code is done by executing the `runnerp1.py` executable, which can be run from the Terminal by,

```bash
$ python runnerp1.py
```

or just

```bash
$ ./runnerp1.py
```

This executes the code in `labp1.py`, and validates the results against some known test vectors.
If you implemented the function right, you will see your names appearing.

### Extra exercise

Change the behavior of `dna2aa` so that it tries all three possible frames of translation, and selects the amino acid sequence that has the longest orf of the three alternatives.
