# Clustering Bacteria Based on Antimicrobial Resistance Gene Composition

## Overview
In this project, we downloaded over 5,000 bacterial reference genomes from NCBI and identified the antimicrobial resistance (AMR) genes present in each. We then clustered the bacteria based on similarities in their AMR gene composition to identify communities with highly similar AMR profiles. Finally, we used Google Gemini to automatically analyze each community and infer potential underlying factors contributing to their shared AMR characteristics.

![image](https://github.com/user-attachments/assets/261cab72-e85f-4ef9-a468-9c347ed6aa47)

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Data Download](#data-download)
- [Environment Setup](#environment-setup)
- [Running the Analysis](#running-the-analysis)
- [Results](#results)
- [License](#license)

## Prerequisites
- [Python](https://www.python.org/)  
- [Anaconda](https://www.anaconda.com/)  
- [RGI (Resistance Gene Identifier)](https://github.com/arpcard/rgi)
- [Gemini API](https://ai.google.dev/)

## Data Download
Download all bacterial reference genomes (complete, reference, typical) from NCBI:

- URL: [NCBI Reference Bacterial Genomes](https://www.ncbi.nlm.nih.gov/datasets/genome/?taxon=2&reference_only=true&typical_only=true&assembly_level=3:3)

Save and extract the downloaded genomes for downstream analysis.

## Environment Setup
Create and activate the Conda environment, then install dependencies:
```bash
conda create -n amr python -y
conda activate amr
conda install seaborn matplotlib numba umap-learn pandas biopython networkx plotly scikit-learn ipykernel google-generativeai -y
```
## Running the Analysis

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/your-repo-name.git](https://github.com/PrittamGoswami/amr_bacteria.git
cd amr_bacteria
```

2. Detect AMR genes in the genomes using RGI:
```bash
python Scripts/rgi_CARD_predict.py
```

3. Construct the clustermap:
```bash
jupyter nbconvert --to notebook --execute --inplace Scripts/clustermap.ipynb
```

4. Detect bacterial communities based on AMR gene similarity:
```bash
jupyter nbconvert --to notebook --execute --inplace Scripts/communities.ipynb
```
5. Analyze each bacterial community using Google Gemini:
```bash
jupyter nbconvert --to notebook --execute --inplace Scripts/communities.ipynb
```
## Results
The clustermap is available at: [link](https://drive.google.com/file/d/1RhwtlLhy3Ry11J4cvgLPSQa6HQVVvrZw/view?usp=sharing)  
The bacterial community plot is available at: [link](https://drive.google.com/file/d/1bNWJ_ZlA9pbfEcDhHUCRhyXs-BgLHRhV/view?usp=sharing)
The Gemini Analysis results is available at: [link](https://drive.google.com/file/d/1dKzFOVWIszvDHzqk-dOR0RylKXObiDR8/view?usp=sharing)
Note: Please submit a request to access the files if you do not have permission.

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE.



