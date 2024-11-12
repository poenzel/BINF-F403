## Training 3
#### 13 Nov 2024

What is ColabFold - [https://github.com/sokrypton/ColabFold](https://github.com/sokrypton/ColabFold)
The importance of single protein prediction and multimer prediction, benchmarking errors and testing working hypothesis. 

[AlphaFold3](https://github.com/google-deepmind/alphafold3) - "free use for academic use" 

<img width="600" alt="Screenshot 2024-11-12 at 22 33 22" src="https://github.com/user-attachments/assets/bfb0fddc-0abb-4fde-a674-d07486e23b19">

[EMBL-EBI AlphaFold Course](https://www.ebi.ac.uk/training/online/courses/alphafold/an-introductory-guide-to-its-strengths-and-limitations/)

### 1. Sequence – structure relationships, protein design, conformational diseases

We will work with a Jupyter notebook in this Practicals 3, using the Google Colab environment. Create a Google Colab environment and import the Jupyter notebook "BINFF403_TP3_ColabFold.ipynb" in this environment.

- [BINFF403_TP3_ColabFold.ipynb](./BINFF403_TP3_ColabFold_colab.ipynb) - Click top left on Open in Colab.

You can also install the Jupyter notebook environment on your own laptop and run the notebook on your laptop, but keep in mind that when the python scripts associated with these Practicals 3 are executed, it will be using your laptop computing power rather than that of Google's servers.

##### You will find in the notebook:
- A modified version of ColabFold, which uses a simplified version of AlphaFold2 to model the structure of a protein sequence. This module provides also an animated picture of the modelled structure, the plDDT score of each residue and the Predicted Aligned Error. The plDDT score is a confidence score of the model. The details of this score and of the Predicted Aligned Error will be explored during Practicals 4 & 5. At this stage, consider that larger is the plDDT score, better is the model.
- An animation module, to analyze the evolution of the modelled structure and its plDDT score along the optimization cycles (if the “recycles parameter” is different to 0).

### 2. Limits of the secondary structures of an experimentally resolved structure

Search for the human thymidylate kinase (PDB code 1E2F) in the protein databank (www.rcsb.org). Search for the secondary structure limits of the protein in PDBSum (http://www.ebi.ac.uk/pdbsum; "Protein" tab, "7 strands" and "11 helices" in the menu on the left). A secondary structure assignation is also provided in the PDB file, sections "HELIX" and "SHEET" (from the PDB website, menu "Display file", "PDB file", find the "HELIX" and "SHEET" sections). Compare both secondary structure assignations (from PDBSum and from the PDB file). Why are they slightly different?

### 2. Sequence – structure relationships

- Read the paper of [Malkov et al. (2008)](https://link.springer.com/article/10.1007/s00894-008-0313-0). Mainly focus on the “Introduction” and the “Results and discussion” sections.
- Use the Table 1 of the paper of Malkov et al. to design the following peptides, and use the tweaked ColabFold tool provided in the notebook “BINFF403_TP3_ColabFold.ipynb” to test the fold of these peptides. First, set the ColabFold “recycles” parameter to 0.

- a peptide of ±20-25 amino acids that folds into an alpha helix;
- a peptide of ±20-25 amino acids that folds into a beta – turn – beta structure;
- a peptide of ±30-35 amino acids that folds into an helix – turn – helix structure.

What is the impact on the structure of the helix if you introduce three Pro or Gly residues in the middle of the helix designed above?

C] Refold the sequence designed above to fold into an helix – turn – helix structure by setting the Colabfold “recycles” parameter to 48. Use the “Animate” module of the notebook to analyze the evolution of the structure and the plDDT score along the 48 cycles.

### 3. Analysis of a part of the prion protein sequence

A. The Creutzeldt-Jakob disease is caused by the aggregation of the prion protein. The structure of the cellular (non pathogenic) prion protein is available in the PDB with the code 1QLX, and contains mainly alpha helices. The aggregated form of the prion protein contains mainly beta strands.

- The files prion_seq1.fasta and prion_seq2.fasta contain the sequence of the prion protein regions 173-194 and 164-228, respectively. Download the PDB file 1QLX from the PDB website and open in Pymol the structure 1qlx.pdb. Which structure is adopted by these sequence regions in the structure of the whole protein ?
- Submit the prion_seq1.fasta sequence to ColabFold (set the “recycles” parameter to 12). Download the modelled structure. For that purpose: click on the “folder” icon on the left of the notebook (see the red arrow on the following figure) 
<img width="944" alt="Screenshot 2024-10-01 at 14 42 19" src="https://github.com/user-attachments/assets/b5c2b1ec-82f5-4ebb-b8da-c8f3ff8116de">

- download the file “out.pdb”, which contains the modelled structure, and rename this file. 

- Submit then the prion_seq2.fasta sequence to ColabFold (set the “recycles” parameter to 12) and download the modelled structure of this second sequence region.

C] Open in a same Pymol window the 1qlx.pdb structure, the modelled structure of the regions 173-194 and 164-228. Compare the structure of the modelled regions to the structure of these regions in the complete protein, 1qlx. To do this:
• Create objects in Pymol containing the corresponding regions in 1qlx. The commands for this are "create region173-194, resi 173-194 and 1qlx” and "create region164-228, resi 164-228 and 1qlx”.
• Use the Pymol Align tool to superimpose the modelled structure of the sequence 173-194 to the region 173-194 of 1qlx.
• Do the same for the region 164-228 and its model.

What is your conclusion ?

---
### Additional 
- [Predicting the structure of large protein complexes using AlphaFold and Monte Carlo tree search](https://www.nature.com/articles/s41467-022-33729-4)
- [AF3 Google Article](https://blog.google/technology/ai/google-deepmind-isomorphic-alphafold-3-ai-model/#life-molecules)
