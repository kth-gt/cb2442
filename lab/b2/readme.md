# LAB B2: rRNA finding, taxonomic classification and multiple sequence alignment

## Preparation questions

Study these questions and bring written answers to the lab. See the ["Practical information"](../readme.md) for more information.

1. What is rRNA? Which organisms have this?
2. How does Blast work?
3. What is “bootstrapping”? How does this procedure estimate the statistical support to the results of an analysis?
4. What is “worse” in a sequence alignment? Substitutions, small gaps or big gaps?
5. How does multiple sequence alignment work? Can you explain the “once a gap, always a gap” rule?

## Instructions and questions

Welcome to the second computer exercise in bioinformatics! In the previous bioinformatics lab, we learned about the epidemic of unknown bacteria. We have found genes in their recently sequenced genomes, and we saw how to use Blast to compare genes to databases in different ways. Today we will start off again by finding genes, but only of a particular kind: ribosomal RNA (rRNA) genes. Ribosomal rRNA is often used for identifying unknown bacteria at a species-level. Go to the [BioToolsBooklet](../biotoolsbooklet.md) and find a tool for identifying rRNA genes. Run your bacterial genome through it.

**Q1** How many rRNA genes did you find? What subunit of the rRNA are they (last column)? How many of each are there?

Download the FASTA results and make a file with just the 16S rRNA gene. This is the subunit that is most commonly used for classification. You will use an online tool for classifying rRNA. Find a tool for doing this in the booklet or online and run it.

**Q2** Is the classification entirely consistent (do all the matches agree with each other)? Does it have strong bootstrap support (in the case your tool gives bootstrap support)?

Look up information on this genus online. Wikipedia might be enough, but look up other websites if you're not convinced.

**Q3** Does it make sense that these patients are so sick? Justify your answers and include your sources.

Now that you know a bit more about your bacteria, we can use this information to compare this new isolate to previously sequenced ones. This might give interesting clues on what is going on. Find in this folder a collection of reference genomes of which one should be your bacterium of interest and download it.

**Q4** Is it likely that very closely related bacterial species will have entire genes added or missing? Why/why not?
*Hint: consider mechanisms of horizontal gene transfer.*

Let's try to see what distinguishes your new genome from others in the species. One way of finding this (albeit not necessarily the most efficient) is through Blast.

**Q5** In which format is the reference genome, nucleotide or protein? What about the file containing the genes you found in the previous bioinformatics lab? In that case, which type of Blast is recommended?

Blast the genes that you found in the previous bioinformatics lab against the reference genome of the bacteria that you chose (reference genomes provided in this lab). Remember to choose a suitable E-value for your search.

**Q6** Which genes do NOT find a good match from this database?
*Hint: open the Blast result in a text editor and use ctrl+F to find empty headers (headers without any matches).* It’s recommended to use a “tabular” output format. See Blast help section for how to choose format. Depending on the version of Blast, you might get the output in the form of:

```verbatim
# BLASTN 2.9.0+
# Query: xxxxx ID= xxxxx
# Database: xxxxxx
# 0 hits found 
```

Find these by searching “# 0” and take note of the query. 

Retrieve only the non-matching genes and make a separate fasta file with them. Submit these to online Blast.

**Q7** Which Blast program did you select? Did you change any parameters from the default values? Which and why?

**Q8** What are the main Blast hits found? Do they explain the toxicity of this new strain of bacteria?

**Q9** From which organism do these genes seem to come from? Does this make sense? Why/why not?

A class of genes that has very important clinical implications is antibiotic-resistance genes. Common mechanisms of antibiotic resistance are pumps that keep the drugs outside the bacterial cell or enzymes that break down the antibiotic, but bacteria can also mutate in a way that makes their own proteins immune to the antibiotics. 

You’ve asked for help from the experts at the sequencing center to characterize the antibiotic-resistance genes in your unknown bacteria. They’ve informed you that it is a multi-antibiotic-resistance operon known as mar. It’s mode of action is still unknown, but some things are already understood. The operon contains 4 protein-coding genes, marA, marB, marC and marR. We’re going to work more with these protein products in later labs. For now, let’s take a closer look at the marB genes.

Download the file called [`MarB.fasta`](MarB.fasta), which contains marB-related proteins from several different bacteria.

We’ll use online Blast again for pairwise sequence comparison. It would take too long to compare each pair of sequences, so we’ll focus on 3 pairs. For each pair you’ll have to choose between blastn, megablast and tblastx as the best tool for aligning them (by best, understand “the tool that gives the most information”). Justify all your answers with your own words as well as the dot-matrix and other pictures from the blast output that you find relevant.

Compare the first sequence, `gb|AF226275.1|:1823-2035`, with the second, `gb|CP003047.1|:1361810-1362022`.

**Q10** Which Blast tool(s) did you pick? Using this, how closely related are these two proteins?

Now compare the first sequence with `gb|CP004887.1|:3422041-3422259`.

**Q11** Which Blast tool(s) did you pick? Using this, how closely related are these two proteins? How does this answer change comparing different tools?

Finally, compare the first sequence with `gi|629665248:741-914`.

**Q12** Which Blast tool(s) did you pick? Using this, how closely related are these two proteins? 

As you’ve noticed, doing pairwise sequence comparisons is quite slow. Fortunately, there are tools for comparing several proteins at the same time. Run this file through a multiple sequence alignment tool. Choose ClustalW format for the multiple alignment, it will make the next steps a little easier.

**Q13** Which multiple sequence alignment tool did you choose? Do the results confirm that the sequences in this file are all related?  Justify your answer with your own words as well as copying parts of the alignment.

Keep this result output open and run one more multiple sequence alignment tool. Choose the same format as before.

**Q14** Which tool did you use now? Do you see any differences in the result comparing the two? Which tool seems better? Justify your answer with your own words as well as copying parts of the alignments.

Now select a relatively conserved part of the multiple sequence alignment and use an online tool for creating a sequence logo.

**Q15** What remarkable characteristics do you see in your logo? Can you make any biological hypothesis about this? Include your logo in the answer.

**Q16** Which sort of information is highlighted in each of these sequence comparison methods: pairwise alignment, multiple alignment and logo? Can you say in which situation you would pick each of these?

**Q17** From a biological perspective, why are there conserved regions or motifs?
