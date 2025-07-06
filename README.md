# Bacterial AMR Gene Clustering Project

This repository provides the necessary resources to reproduce the analysis of antimicrobial resistance (AMR) gene profiles across bacterial reference genomes.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Data Download](#data-download)
- [Environment Setup](#environment-setup)
- [Running the Analysis](#running-the-analysis)
- [Results](#results)
- [License](#license)

## Overview
In this project, we downloaded all bacterial reference genomes from NCBI and detected the antimicrobial resistance (AMR) genes present in them. We then clustered bacteria based on their similarity in AMR gene composition, aiming to identify bacterial communities with highly similar AMR profiles.

## Prerequisites
- Python  
- [Anaconda](https://www.anaconda.com/)  
- [RGI (Resistance Gene Identifier)](https://github.com/arpcard/rgi)

## Data Download
Download all bacterial reference genomes (complete, reference, typical) from NCBI:

- URL: [NCBI Reference Bacterial Genomes](https://www.ncbi.nlm.nih.gov/datasets/genome/?taxon=2&reference_only=true&typical_only=true&assembly_level=3:3)

Save and extract the downloaded genomes for downstream analysis.

## Environment Setup
Create and activate the Conda environment, then install dependencies:
```bash
conda create -n amr python -y
conda activate amr
conda install seaborn matplotlib numba umap-learn pandas biopython networkx plotly scikit-learn ipykernel -y
```
## Running the Analysis

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Detect AMR genes in the genomes using RGI:
```bash
python Scripts/rgi_CARD_predict.py
```

3. Construct the clustermap:
```bash
jupyter nbconvert --to notebook --execute --inplace Scripts/5.bulk_transcriptomic_analysis.ipynb
```

4. Detect bacterial communities based on AMR gene similarity:
```bash
jupyter nbconvert --to notebook --execute --inplace Scripts/communities.ipynb
```

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE.



