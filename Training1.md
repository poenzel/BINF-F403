### Training 1
#### 30 Oct 2024

### 1. Quality of experimental structures

A] Find on the Protein Databank website (http://www.rcsb.org) the proteins with the PDB code
1N0S and 1T0V. Which experimental method has been used to obtain them ? What are the
values of the resolution and of the R factor (R-value) of the X-ray structure ? What is the
difference between R-value and the R-free ? How much conformers are there in the PDB file
of the NMR structure ?

B] Compare the quality of both structures. Use for that purpose the full report of the "Structure
validation" section; focus on sections "Overall quality at a glance", "Residue property plot" and
"Model quality / Torsion angles / Protein backbone" of this report. In the "Residue property
plot" section of the report for 1N0S, what does a red dot on the figure mean? Which residues
are marked with a red dot?
Analyze also the Procheck report of each structure. This Procheck report is available on
PDBSum (http://www.ebi.ac.uk/pdbsum).

### 2. Asymmetric unit and biological assembly

For the 1N0S structure: how many chains are there in the asymmetric unit and in the biological
assembly? This information is available at the top left of the 1N0S page. What is the difference
between the asymmetric unit and the biological assembly?
Note that you can download either the asymmetric unit or the biological assembly from the
"Download Files" menu.

### 3. Visualization of structures

The Pymol software will be used to visualize the structures. The Pymol software and a user
manual are provided on the Virtual University.

A] Download the PDB files of 1N0S and 1T0V (menu on the right, "Download files – PDB
text"). 

```
fetch 1N0S
fetch 1T0V
```

Open 1N0S in Pymol. Test the menus on the right (A-S-H-L-C). Show the protein with
the "Cartoon" representation (menu "S"). 

```
select 1T0V
show cartoon
```

Select the chain A of the protein ("select xxx, chain A", where xxx is the name of the menu that will be created for the selected items), and represent this chain in a different color (menu "C").

```
select 1T0V
select chain A
show cartoon
show sticks
colour paleblue
```


Hide the "Cartoon" representation (menu "H") and show the sticks representation.

B] Download the electronic density file of 1N0S from the Virtual University: 1n0sM1.ccp4.
This file has been obtained from the "Electron Density Server". Open this file in Pymol. In the
"A" menu of 1n0sM1, choose "Mesh", with the level 1.0. Then, modify the level to 1.5 ("A"
menu of the "_mesh" menu that has been created). Select one of the amino acids that is marked
by a red dot in the "Residue property plot" section of the validation report (see section 1B) and
zoom on this residue (Menu "A", "zoom"). Is there a good conformity between the electron
density of this residue and the position of its atoms?

C] Erase the electronic density and open the 1T0V file in Pymol. Align 1T0V and 1N0S (menu
"A" of 1T0V – align – to molecule – 1N0S). Zoom on the superimposed structures (menu "A"
– zoom). Erase 1N0S. Show the "Cartoon" representation of 1T0V. Analyze the structure of the
20 conformers of this NMR structure (menu at the bottom right of the Pymol window, use the
arrows to visualize the different conformers).

### 4. Enzyme-ligand complex

Erase the previous work in Pymol: "File – reinitialize".
A] Download from the PDB the structure file of dihydrofolate reductase in complex with
trimethoprim (PDB code 1DG5). Submit this PDB code to the PDBSum website
(http://www.ebi.ac.uk/pdbsum/). Which amino acids are in interaction with trimethoprim (the code "TOP" corresponds to this ligand; go in the left menu, section "Ligand").

B] Open the PDB 1DG5 in Pymol. Show the surface of the protein. Select the amino acids that
are involved in the interaction with the ligand (see section 3A): "select inter,resi x+y+z", where
x, y, z, … are the number of the identified amino acids and "inter" is the name of the menu that
will correspond to the selection (you can choose this name). Color these amino acids. Select
the trimethoprim ("select trim, resn TOP") and show this selection by using the "Sticks"
representation and color this selection. Analyze the surface of the protein and the position of
the ligand.

C] Show the protein in "Cartoon" and the amino acids that interact with the ligand in "Sticks".
Analyze the distance between them (take the atoms that interact): use the menu "Wizard" (at
the top of the Pymol window) and then "Measurement".

5. Compactness of the protein core
A] Select the amino acid number 100 of 1DG5 and use a "Sticks" representation (give a name
to this selection). Select then the surrounding of this residue: "menu A of the selection – modify 
– around – residues within 5 A". Show these amino acids in "Sticks". We will mutate this core
amino acid to illustrate the protein compactness. Use the menu "Wizard – Mutagenesis". In the
new menu on the right of the Pymol window, choose a mutation into phenylalanine (Phe), then
click on the amino acid number 100. You can test the different possible conformers of the side
chain with the arrows on the bottom right of the Pymol window. The red disks show the steric
clashes.



---
### References 
- [PyMol Command Reference](https://pymol.org/pymol-command-ref.html)
- [Practical PyMol for beginners](https://pymolwiki.org/index.php/Practical_Pymol_for_Beginners) - PyMol Wiki
