# NCBI Datasets CLI Usage Guide

## Overview
This project provides examples on how to retrieve viral genomic data from the [NCBI Datasets](https://github.com/ncbi/datasets) using both the command-line interface (CLI) and programmatic access through Python. The focus is on obtaining metadata and genomic sequences for the **Dengue virus** using its taxonomic and accession identifiers.

## Installation
To use the NCBI Datasets command-line interface (CLI), install it via Conda:

```bash
conda install -c conda-forge ncbi-datasets-cli
```

## Downloading Viral Genomic Data

### By Taxonomic ID
You can download genome data using the virus taxon ID. For example, the **Dengue virus** has a taxon ID of `12637`:

```bash
datasets download virus genome taxon 12637 --filename dengue_126437.zip
```

### By Accession ID
Alternatively, you can download specific viral genome sequences using their accession IDs:

```bash
datasets download virus genome accession PQ844993.1 --filename PQ844993_1.zip
datasets download virus genome accession ON634724.1 --filename ON634724_1.zip
```

## Extracting Metadata
The metadata for each genome sequence is stored in a `.jsonl` file, which contains a list of JSON objects corresponding to each accession number. You can convert this JSONL file into a tab-separated values (TSV) file using the `dataformat` command:

```bash
dataformat tsv virus-genome --inputfile dengue_126437/ncbi_dataset/data_report.jsonl >> results/dengue_126437.tsv
dataformat tsv virus-genome --inputfile PQ844993_1/ncbi_dataset/data_report.jsonl >> results/PQ844993_1.tsv
```

## Using the NCBI API
This project also includes Python scripts demonstrating how to interact with the NCBI Datasets API to retrieve taxonomy and genome data programmatically. The script:

- Queries the taxonomy API for a given virus name
- Retrieves the taxonomic ID
- Uses the taxonomic ID to request available genome data
- Downloads the metadata from the API

## Summary
This project provides two approaches for accessing NCBI virus genome data:

1. **Command-line approach:** Uses `ncbi-datasets-cli` to download genome sequences and metadata.
2. **Programmatic approach:** Uses Python to query the NCBI API and download genomic metadata dynamically.

This setup enables efficient retrieval and processing of viral genome data for bioinformatics and research applications.

