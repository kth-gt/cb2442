# Programming Lab P4 - Making a tree using UPGMA clustering

Hierarchical clustering is widely used in bioinformatics. In the CB2442 course, you have encountered it both in the Sequence feature module and in the Phylogenetics module. In this lab, your task is to write a function that, given a pairwise distance matrix and a list of names of the corresponding objects (in this case, sequences), performs hierarchical clustering using the Unweighted Pair Group Method with Arithmetic Mean (UPGMA) method. The function should output the result as a tree in the Newick format. **Before starting, please read this thoroughly**

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
that takes a pairwise distance matrix (as a 2-dimensional [numpy array](https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp)) and a list of sequence names (as a [list](https://www.w3schools.com/python/python_lists.asp)) as input and should return a tree in [Newick](https://en.wikipedia.org/wiki/Newick_format#:~:text=In%20mathematics%2C%20Newick%20tree%20format,Maddison%2C%20Christopher%20Meacham%2C%20F.) format (as a [string](https://www.w3schools.com/python/python_strings.asp)). The output tree should not include branch lengths. Also, set the list `authors` in the beginning of the file to contain the group members' names.  


### Algorithm Steps
1. **Initialization**:

   - **`nwk_list`**: A list containing the names of the sequences (e.g., `['S1', 'S2', 'S3', ...]`). 
   - **`cluster_list`**: A list of lists, each with a single sequence index (e.g., `[[0], [1], [2], ...]`). This is the same as the **`nwk_list`** but it has indices instead of names.
   - **`updated_dist_matr`**: A copy of the original distance matrix (`dist_matr`) that will be **modified** during clustering.

2. **Iterative Clustering**:

   - **While** there is more than one cluster in `cluster_list`:
     - **Find the pair of clusters with the smallest distance** in `updated_dist_matr`. Remember that each row/column represents a cluster!
     - **Merge Clusters**:
       - Create a new cluster by combining the indices of the two closest clusters. `[0,1]`
       - Remove the clusters that you merged from `cluster_list`.  `[[0], [1], [2], ...]` --> `[[2], ...]`
       - Append the new merged cluster to `cluster_list`. `[[2], [0,1], ...]`
     - **Update `nwk_list`**:
       - Combine the Newick strings of the two clusters (e.g., `'(S1,S2)'`).
       - Remove the old entries from `nwk_list`.
       - Append the new Newick string to `nwk_list`.
     - **Update `updated_dist_matr`**:
       - Remove rows and columns of the merged clusters.
       - Add a new row and column for the new cluster initialized with zeros (this step is already done for you).
       - Compute the average distances between the new cluster and the remaining clusters. This way you can fill the new row and column added previously. If you find this tricky refer to the "updating the distance matrix" section.
### Debugging Tips
- **Printing statements** for the `cluster_list`, the `nwk_list`, and the `updated_dist_matr` to check they are changing according to your plan.
- Think about what the smallest cluster distance means. Does it make sense to take the smallest distance for `i=j`?
- Think about the distance matrix being symmetric. Does it mean there is redundancy in the data?
- Make sure you know how to get array and list indices. Stack overflow can be a good source
- Make sure you know how to add and delete elements from a list/array in Python. When you delete an element, be careful with the index order!
- Be careful with the iterators in the `for` loops, and make sure they are behaving as you want. Python starts at `0` and finishes at `len-1` by default, but it can be changed.

### Updating the Distance Matrix
The last step is to update the distance matrix by filling the row and column initialized at values of `0`.

For each other cluster:

1. Look at every sequence in the new cluster.
2. Look at every sequence in the other cluster.
3. Find the distance between each pair (one from the new cluster and one from the other cluster) **from the original distance matrix** (`dist_matr`).
4. Add all these distances together.
5. Divide the total by the number of comparisons (i.e., the number of pairs). 

This gives you the average distance between the new cluster and the other cluster. 

Repeat for every other cluster.


### Test

You can make an initial execution of your `upgma` function by running the main function of the python file itself by executing the line

```bash
$ python3 labp4.py
```

However, the final test of the code is done by executing the `runner4.py` executable, which can be executed from command line as

```bash
$ python3 runner4.py
```

or just

```bash
$ ./runner4.py
```

This executes the `upgma` function in `labp4.py` using a couple of test inputs and validates the results.
If you have implemented the function correctly, you will see your names appear.

Good luck with the lab!
