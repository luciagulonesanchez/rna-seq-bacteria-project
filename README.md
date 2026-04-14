# rna-seq-bacteria-project
Analysis of bacterial RNA-seq data to study differential gene expression under antibiotic stress conditions.

## Description 
This project aims to analyze RNA-seq data from *Staphylococcus aureus* by comparing samples with and without exposure to vancomycin. 
The analysis focuses on identifying changes in gene expression when the bacteria are under the effect of the antibiotic. 
More information about RNA-seq can be found here: [RNA-seq (Nature article)](https://www.nature.com/articles/nrg2484) 
## Objective 
The main objective is to identify genes whose expression is altered in the presence of vancomycin, with particular interest in those involved in:

- Antibiotic resistance mechanisms  
- Cellular stress response  
- Cell wall synthesis and remodeling processes  
- Efflux pump systems
  
To achieve the proposed objectives, the following bioinformatics analyses will be carried out:
- Differential gene expression analysis between conditions (with and without antibiotic)  
- Identification of significantly upregulated and downregulated genes  
- Visualization of results using volcano plots  
- Visualization of expression patterns using heatmaps of significant genes

![RNA-seq workflow](https://github.com/user-attachments/assets/f550ce50-939f-41c6-a8b3-cab65f905303 "RNA-seq workflow")

Figure 1. Workflow of RNA-seq analysis. 

   
## Project structure
The repository is organized into different folders to facilitate workflow and reproducibility:

- **data/**: contains the data used in the study (raw and processed data).
- **scripts/**: includes scripts used for bioinformatics analysis.
- **docs/**: additional project documentation.
- **notebooks/**: contains Jupyter Notebooks used for interactive data analysis, exploration, and visualization.
- **results/**: contains the results obtained from different analyses. This folder is organized into two subfolders: 'tables/', which includes tables with the main analysis results and 'figures/' which contains the visual representations of the results.
 
## Tools Used 
The project was developed using the following tools for data analysis and version control:
- **Python**: used for data processing, differential expression analysis, and visualization.
- **GitHub**: used for version control and collaborative work.
- **Jupyter Notebook**: used for interactive analysis.
