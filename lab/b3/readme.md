# LAB B3: Protein sequence feature prediction, multiple sequence alignment and phylogenetics

## Preparation questions

Study these questions and bring written answers to the lab. See the ["Practical information"](../readme.md) for more information.

1. Based on just the hydrophobicity/hydrophilicity of the amino acid side chains, which parts of the hypothetical membrane protein LIFIRDNDEPTLIF will be inside the membrane and which will be outside?
1. Look up what the Hamming distance is and calculate the Hamming distance between the aligned sequences (where a "-" indicates a deletion):  
  
   ```verbatim
   PRI-LFDNRLDEFL  
   DRINLFRNR--NRL
   ```

1. Look up how the UPGMA clustering method works and draw the dendrogram for the following distance matrix:

|    | Seq1 | Seq2 | Seq3 | Seq4|
|----|:---:|:---:|:---:|:---:|
Seq1 | 0 | 2 | 6 | 5 |
Seq2 | 2 | 0 | 1 | 10 |
Seq3 | 6 | 1 | 0 | 4 |
Seq4 | 5 | 10 | 4 | 0 |

## Instructions and questions

In the previous lab, we used Blast and multiple sequence alignment to find foreign genes in our pathogenic bacterium. We learned that the cause of the epidemic were foreign toxins and also that the bacteria had some antibiotic resistance genes. Today, we’ll take a closer look at these genes by using different approaches and tools for protein sequence feature prediction.

As was mentioned in the previous lab, one of the mechanisms of antibiotic resistance is the use of so-called efflux pumps in the cellular membrane. Transmembrane proteins have very characteristic properties in their sequences, which allow us to identify them and do some rough predictions on their structure (which parts are inside the membrane and which parts are in- and outside the cell). 

In the previous lab you found some non-matching genes in the bacterial genome you chose to examine. Four of these corresponded to antibiotic resistance genes and two to a toxin. If you did not find these six genes in the previous lab, use the files [AB_Resistance_GeneMarkS_proteins.fasta](AB_Resistance_GeneMarkS_proteins.fasta), [toxin_Bact1_aminoacids.fasta](toxin_Bact1_aminoacids.fasta), [toxin_Bact2_aminoacids.fasta](toxin_Bact2_aminoacids.fasta), and [toxin_Bact3_aminoacids.fasta](toxin_Bact3_aminoacids.fasta).

Run one of the tools from the [Bioinformatics tools booklet](../biotoolsbooklet.md) to find out if any of the antibiotic resistance genes have a transmembrane efflux pump candidate. Note that you might have to translate the nucleotide sequence to an amino acid sequence for the tool to work.

**Q1** Which tool did you use? Which of the genes had TM helices? What is the 2D structure of this candidate (e.g. how many TM helices are there; does the protein start/end inside/outside the cell)?

One way of finding out the function of a protein is to search the InterPro database, which contains information about the functionality of protein families and domains and their protein structure. Upload any potential efflux pump candidates (genes with TM helices) to the InterPro website. 

**Q2** What protein domain/family does your candidate match to? What is its functionality? 

**Q3** Do you think your candidate protein is an efflux pump? Why or why not?

Another way to increase antibiotic resistance is by up- or down-regulation of genes that influence the antibiotic pathway. Check all the other antibiotic resistance genes in InterPro to see if this mechanism is present in one or more of them.

**Q4** Which families/domains did you find in InterPro (for the other genes)? What are their functions?

**Q5** Which of these domains play a role in gene regulation?

Another way to get more detailed information about proteins of interest is to search them against the UniProtKB database.

**Q6** What is the difference between the InterPro and UniProtKB databases? When do you use which?

We could go directly to the UniProtKB website and run a Blast search there, but there is actually a nice way to get to all protein information through the NCBI Blast search engine website:

Run a Blast protein search (blastp) on the antibiotic resistance genes against the “UniProtKB/SwissProt” database for each protein serparately. Copy the first part of the accession number of your top hit (e.g. P0A2S4 not P0A2S4.1) and search on it in the UniProtKB website (uniprot.org) to get more information on the hit. **Hint: look under "Family & Domains"

**Q7** Which domain is present in multiple (2 or more) proteins? How does this domain do its job?

The fact that we observe this domain already multiple times in such a small set of proteins shows the power of using recurring protein domains to infer the functionality of (parts of) proteins.

**Q8** How can we use the information we extracted about the antibiotic resistance proteins to improve the treatment of our patients?

Now that we know more about the antibiotic resistance genes, it is time to focus our attention on the toxin. We can start by trying to find toxins from other bacteria that are related to the toxin you found as a non-matching gene in lab 5.

**Q9** How could finding related toxins help us to improve the treatment of our patients?

We will use PSI-BLAST (a type of protein blast) to look for distant relatives of your toxin in as many different species as possible. Run the first iteration of your PSI-BLAST search with a maximum of 50 target sequences against the nr database for the first gene of the toxin. Exclude the organism the toxin originates from and *Escherichia coli* from the BLAST search, this will help to get a more diverse set of related toxins in different organisms.

**Q10** What is the best match and what is its E-value?

Now keep running iterations until the algorithm has converged, i.e. until very few (< 2) new hits highlighted in yellow show up in the top 50.

**Q11** What is the best match now and what is its E-value? Why has it changed?

Take approximately 10-20 matches from different (sub)species and create an unaligned FASTA file with these. Also include the original toxin sequence from your bacterium. Change each of the sequence titles in the FASTA file to the (sub)species' names, this will make the coming analysis much easier. Now we will build a phylogenetic tree of the sequences to get an idea of the evolutionary relationship of the toxin in the selected (sub)species. The field of phylogenetics has a wide range of bioinformatics tools available. Here we will use the online portal Phylogeny.fr [www.phylogeny.fr]. Select “A la Carte” under “Phylogeny Analysis”. Here you can specify options for the different steps of the analysis. Select “ProtDist/FastDist + Neighbor” for construction of the phylogenetic tree and choose all other options as you wish. Create the workflow and paste in or upload your FASTA file with the toxins.
 
**Q12** Which multiple sequence alignment algorithm did you use? Why did you choose it over the others?
 
**Q13** Which species has the closest related toxin according to your tree? Are there any other (sub)species sharing the most recent common ancestor of these two? Include the tree in your answer!
 
**Q14** Which genus (other than the one of our toxin) would you advise to investigate next?

**Q15** You used the Neighbor-Joining method for constructing the tree. In what way is that different from the UPGMA method that you used in the preparatory question?
 
Producing a nice looking tree is one thing, but, in order to draw any conclusions from it, a more important question is: how confident are we in the results?

**Q16** The Neighbor-Joining method you used here applies the “JTT model” for measuring distances between the protein sequences. That means a JTT matrix, similar to the PAM matrix (see Clair and Visick page 84) is used for scoring the alignment between a pair of sequences. Why is this measure better than simply counting what percentage of amino acids are different between the pair of sequences?

**Q17** What information can we deduce from the lengths of the branches?

**Q18** How confident are we in the whole tree structure as an evolutionary tree for that matter? Is there a way to give statistical support to back up this confidence (or lack thereof)?

To obtain phylogenetic trees of species, it is common to look at conserved, rarely laterally transferred genes, like the rRNA genes.

**Q19** Would a phylogenetic tree based on rRNA gene sequences from the same bacterial species be similar to the one that you have just created? What do you think would be similar and what would change? Why?

**Q20** A phylogenetic tree can be used to identify related bacterial species, which, in turn, may help us discover new treatment options for our disease. From a pharmacological standpoint, which tree would be most useful in this regard? Give an argument for both the tree based on the toxin and a tree based on rRNA gene sequences!
