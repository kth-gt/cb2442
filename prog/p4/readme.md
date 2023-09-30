# Programming Lab P4 - Making a tree using UPGMA clustering

Hierarchical clustering is widely used in bioinformatics. In the CB2442 course, you have encountered it both in the Sequence feature module and in the Phylogenetics module. In this lab, your task is to write a function that, given a pairwise distance matrix and a list of names of the corresponding objects (in this case, sequences), performs hierarchical clustering using the Unweighted Pair Group Method with Arithmetic Mean (UPGMA) method. The function should output the result as a tree in the Newick format.

### Installation

Begin with downloading the project to your local computer by using this [link](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fkth-gt%2Fcb2442%2Ftree%2Fmain%2Fprog%2Fp4). 


Unzip the files into a directory and open the directory in VScode. 
```bash
$ unzip 'kth-gt cb2442 main prog-p1.zip'
$ code .
```

### Implementation

In the `labp4.py` file, modify the function

```python
def upgma(dist_matr, names_list):
```
that takes a pairwise distance matrix (as a 2-dimensional [numpy array](https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp)) and a list of sequence names (as a [list](https://www.w3schools.com/python/python_lists.asp)) as input and should return a tree in [Newick](https://en.wikipedia.org/wiki/Newick_format#:~:text=In%20mathematics%2C%20Newick%20tree%20format,Maddison%2C%20Christopher%20Meacham%2C%20F.) format (as a [string](https://www.w3schools.com/python/python_strings.asp)). Also, set the list `authors` to contain all the group members' names.  

### Test

You can make an initial execution of your `upgma` function by running the main function of the python file itself by executing the line,

```bash
$ python3 labp4.py
```

However, the final test of the code is done by executing the `runner4.py` executable, which can be executed from command line as, 

```bash
$ python3 runner4.py
```

or just

```bash
$ ./runner4.py
```

This executes the code in `labp4.py`, and validates the results against some test examples.
If you implemented the function right, you will see your names appearing.

### Extra excercise

