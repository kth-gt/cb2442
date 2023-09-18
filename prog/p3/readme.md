# Programming Lab P3 - Gene expression

## Introduction

Your task is to code a Python program that calculates RPKM and also TPM
(task #1), and that generates a scatter plot of RPKM versus TPM (task
#2). There is also an optional third task (#3). You are given two input
files, described below, and a code "skeleton" on which you should build
your program. The output should be (1) a file that contains the ID or
name of each annotated gene and its RPKM and its TPM and (2) a plot in
the png format.

RPKM and TPM are defined in the Sequence features module, topic RNA-seq.
In Canvas there is a handout and a link to the recorded lecture about
Gene expression and RNA-seq.

### The biology

The spruce ("gran" in Swedish) is a tree that sets cones ("bildar
kottar", in Swedish) every 3-5 years after a juvenile period of roughly
20 years. In a collaboration with the Swedish University of Agricultural
Sciences ([SLU](https://www.slu.se)), we investigate the molecular
mechanisms of cone setting in both normal spruce ("wild type") and in a
naturally occurring mutant named acrocona, which has the phenotype that
it sets cones already at age 3 years, and then almost every year after
that. The aim of the research project is to detect what genes that are
involved in the onset of cone formation, and how these are regulated. In
this programming exercise, we will use processed RNA-seq data from wild
type trees.

#### The data

The data is available in the file read_counts.tsv: this file contains
RNA-seq read counts from three different samples of female cones very
early in their development. The three different samples are named S1,
S2, and S3. In this programming task, you will work with S1, and may
thus disregard from the S2 and S3 columns. The reads have been mapped by
minimap2 to the annotated genes (see below) of spruce (Picea abies)
[reference genome version 1.0](https://treegenesdb.org/org/Picea-abies),
and then the reads mapped to each gene have been counted. Whenever a
read mapped to two or more genes, it was kept as a match in both.
The read_counts.tsv file looks like this (rows 1-5 of 51,040):

| #Gene_ID | count_S1 | count_S2 | count_S3 |
| ------ | ------ | ------ | ------ |
| MA_10000213g0010.1 |  4 |  0 |  2 |
| MA_10000405g0010.1 |  1 |  0 | 11 |
| MA_1000049g0010.1  |  0 |  2 |  1 |
| MA_10000516g0010.1 | 11 | 10 | 19 |

### The annotation:

The annotation file cds_lens.tsv contains the length of all the genes.
Note that this is a very allowing list of genes - it contains 66632
genes, many of which are probably not correct, and might also be
duplicates of each other (recall from the genome assembly lecture that
the spruce genome version 1.0 is not in a very good shape). In brief,
this is not a set of high-confidence genes. The cds_lens.tsv file is a
processed version of an actual annotation file (in the gff format). We
did the processing for you so you can focus on the tasks #0, #1, and #2.
The cds_lens.tsv file looks like this (rows 1-5 of 66,633):

| #Gene_ID | Gene_len |
| ------ | ------ |
| MA_10000213g0010.1  | 738 |
| MA_10000405g0010.1  | 917 |
| MA_1000049g0010.1   | 399 |
| MA_10000516g0010.1  | 354 | 

### The output

Two output files should be created: one "tab-separated" data file with
gene name, RPKM and TPM values, and one png with the scatterplot of RPKM
vs TPM. See below for more details.

## Preparations

### Installation

Task #0: Before you start programming:

(a) install the library 'matplotlib'. You will need it for task #2. Install it like this:
```bash
$ conda install matplotlib
```

Instructions regarding the use of Miniconda - and hence the conda
command - in this course are [here](../lab/software_installation_manual.md)

(b) download the project files to your local computer by using this [link](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fkth-gt%2Fcb2442%2Ftree%2Fmain%2Fprog%2Fp3).

Unzip the files into a directory and open the directory in VScode. 
```bash
$ unzip 'kth-gt cb2442 main prog-p3.zip'
$ code .
```

## Implementation

Edit the file labp3.py and add your own code

Set the list `authors` to contain all the group members names.  

Task #1: Calculate (a) RPKM and (b) TPM for all the genes listed in the
annotation file.
This should be output in a file that contains (i) a header line that
names the columns, (ii) one line for each gene listed in the annotation
file, where each line has three fields: Gene name, RPKM, and TPM, and
these should be separated by tabs ("\t").

Note: not all genes in the annotation file are in the data file. This is
because not all genes have reads that mapped to them. Simply because not
all genes are expressed in the sample. You should handle this situation
in your code and set RPKM/TPM to zero for these genes. The Python data
structure dictionaries is useful here (see the [Python documentation]
(https://docs.python.org/3/tutorial/datastructures.html#dictionaries)).

Task #2: Create a scatterplot of TPM versus RPKM values for all the genes.
One datapoint for each gene, where the x-value of the datapoint is the
RPKM and the y-value of the datapoint is the TPM. The plot should be
created in png format, and you should set an appropriate plot title as
well as appropriate labels on the x and y axes. Here is where you need
the library 'matplotlib' installed (see task #0).

Task #3 - optional
If you did tasks #1 and #2 and you still have time left, you could
continue with these suggestions:
(a) change your code so that you can get the counts and perform the RPKM
and TPM calculations for all three samples (S1, S2, S3), and output RPKM
and TPM values for all three samples in one file.
(b) plot the RPKM (or TPM) of S1 vs S2 (or any other combination of the
three samples).
(c) calculate the correlation coefficient (r) (see [wikipedia](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)) of the
same datasets you used in (b). Make sure you have numpy installed (you
should have this from the previous lab), and also [scipy](https://scipy.org/)
which provides a lot of algorithms for, among many
other things, statistics. Don't forget to add scipy to your script:
import scipy as sp
You can of course also code the correlation coefficient calculation on
your own and not use scipy.

## TEST

You can run your code by executing the command
```bash
$ python labp3.py cds_lens.tsv read_counts.tsv > my_output_file.tsv
```
Where my_output_file.tsv is the name of the file in which the RPKM and TPM values will be output. The name of the file with the scatterplot is set inside the labp3.py script with the plt.savefig() function.

The first lines of the output file ("my_output_file.tsv") with RPKM and TPM should look like this. Use this to test if your implementation of the algorithms is correct. Note that here, RPKM and TPM values are presented with 3 decimals (in your implementation, you might have chosen a different handling of the decimals). 

| #Gene_ID | RPKM | TPM |
| ------ | ------ | ------ |
| MA_10000213g0010.1  | 0.232 | 0.142 |
| MA_10000405g0010.1  | 0.047 | 0.029 |
| MA_1000049g0010.1   | 0.000 | 0.000 |
| MA_10000516g0010.1  | 1.333 | 0.814 |

The scatterplot should be in the png format. 

