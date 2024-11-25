## Training 4 and 5

### 3D structure modelling
### 27 Nov 2024 and 4 Dec 2024

This practical focuses on the modelling of protein structures by comparative modelling and by
a version of AlphaFold2. You will create different models for the acyl carrier protein of
Rhodospirillum centenum. The quality of your models will be evaluated with QmeanDisco and
Procheck. These tools are available here:

• QmeanDisco: https://swissmodel.expasy.org/qmean/

• Procheck, via "PDBSum Generate": https://www.ebi.ac.uk/thornton-srv/databases/pdbsum/Generate_on.html


What is the QmeanDisco score based on and how to interpret its value? Use the following
documents to answer this question:

• https://swissmodel.expasy.org/qmean/help

• Information about lDDT score is available here: https://swissmodel.expasy.org/lddt/help/#overview

A plDDT score is also provided for AlphaFold models. Use the following documents to
interpret the plDDT score:

• Supplementary material of the AlphaFold paper, section 1.9.6 page 37 (the document is
on the Virtual University).

• FAQ https://alphafold.ebi.ac.uk/faq section “How confident should I be in a
prediction?”

### 1. Comparative modelling of the 3D structure of the acyl carrier protein of Rhodospirillum centenum: manual approach

The uniprot code of the acyl carrier protein of Rhodospirillum centenum (ACP) is B6IN76; its sequence is available in FASTA format on Uniprot (http://www.uniprot.org). In this first section, you will do manually each step of a comparative modelling: search of possible templates, selection of a template, sequence alignment between the target and the template, modelling and evaluation of the quality of the model.

A] Perform a Blast (http://www.ncbi.nlm.nih.gov/blast/; use "Protein blast") on the ACP sequence to identify a template to model the structure of this protein (choose the appropriate database to scan with BLAST). 

B] Select a template among the hits that have been identified by Blast. For that purpose, take into account the percentage of sequence identity, the percentage of query cover and the quality of the structure of the template (see the tools used in Practicals1). Download the sequence of the template from the PDB website.

C] Perform a sequence alignment between the template and ACP. For that purpose, use the Needle global alignment program (https://www.ebi.ac.uk/jdispatcher/psa/emboss_needle, choose the "Markx3" output format in the "Parameters" menu).

D] Submit the sequence alignment obtained in the section 1.C. to the Modeller server (https://toolkit.tuebingen.mpg.de/#/tools/modeller). The license key to use Modeller is "MODELIRANJE". The sequence alignment must be provided in PIR format. There is on the virtual university a document that explains how to convert the Markx3 format obtained from the sequence alignment into a PIR format that must be submitted to Modeller.
Save the PDB file of the model.

E] Analyze the quality of this model.

### 2. Comparative modelling of the 3D structure of the acyl carrier protein of Rhodospirillum centenum: semi-automatic approach
The HHPRed server combined to Modeller (https://toolkit.tuebingen.mpg.de/#/tools/hhpred) will be used.

A] Submit the ACP sequence to the HHPred server. Describe the first step performed by HHPred. Several templates are proposed. Compare these templates to those identified with Blast in section 1.B. (sequence identity, quality of the template structure, …).

B] Select the first template and click on "Model using selection". HHPred will align the 2 sequences. Then click on "Forward to Modeller", use the Modeller-key "MODELIRANJE" and click on "Submit job". Save the PDB file of the model (you will find a "Download PDB file" tab).

C] Analyze the quality of this model.

### 3. Comparative modelling of the 3D structure of the acyl carrier protein of Rhodospirillum
centenum: automatic approach
Use the SwissModel server (https://swissmodel.expasy.org) to build a model of ACP. Select a
different template than that used in sections 1 and 2. Identify the template that has been used. Save the PDB file of the model. Analyze the quality of this model.

### 4. Modelling of the 3D structure of the acyl carrier protein of Rhodospirillum centenum with ColabFold

The ColabFold Jupyter Notebook is available here: https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

A] Read the “Instructions” section at the end of the notebook. What are the defaults settings for
“template_mode” and “MSA options” ?

B] Copy-paste the sequence of the acyl carrier protein of Rhodospirillum centenum in the
“query_sequence” field of the notebook. Keep all the default settings.

C] You will obtain a zipped file that contains the results. Unzip this file. Open the log.txt to
have the plDDT score of the different models. Select the PDB file of the model with the best
plDDT score.

D] Submit a second query, by choosing “pdb100” as template_mode and num_relax=1. You
will obtain a second zipped file that contains the results. Unzip this file. Open the log.txt to
have the plDDT score of the different models. Select the PDB file of the model with the best
plDDT score.

E] Analyze the quality of these two models with Qmean and Procheck.

### 5. AlphaFold model

An AlphaFold model is available on the Uniprot page of the protein (“Structure” section).

A] Download the PDB file of the AlphaFold model from Uniprot.

B] Evaluate the quality of this model.

### 6. Comparison of the models

You now have 6 models for ACP: 3 obtained by comparative modelling, 2 by ColabFold and one by AlphaFold.

A] Compare the quality of these models by using their Qmean and Procheck scores.

B] Open the 6 PDB files of the models in a same window in Pymol. Write a python script to be run in Pymol to calculate the rmsd between all pairs of structure. For that purpose:

• you can use the "super" command in pymol. To superimpose the main chain atoms of struc1 to those of struc2 and to compute the rmsd, for instance, use the command "super struc2 and name ca+c+o+n,struct1 and name ca+c+o+n,cycles=0". Read the documentation about the "super" command.

• Pymol can execute scripts written in Python. To execute a given script, “scr.py” for instance, : write “run scr.py” in the command line of Pymol. The commands that could be useful in the script are : cmd.get_names(), cmd.super(), len(). You can also use the Pymolwiki to get more information.

Group the models according to their structural similarity (evaluated by the rmsd value).

C] Use the "super" command, to superimpose all the models on one the 5 models and to identify the regions where the structural differences are the largest.
---
### References
