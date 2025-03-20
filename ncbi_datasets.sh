# install the library for the NCBI Datasets command line interface
# conda install -c conda-forge ncbi-datasets-cli

# we can download data by the virus taxon id: in this case the dengue virus
datasets download virus genome taxon 12637 --filename dengue_126437.zip 

# we can download data by the virus accession id: in this case the dengue virus
# the data will be saved in a zip file
datasets download virus genome accession PQ844993.1 --filename PQ844993_1.zip #Check on: https://www.ncbi.nlm.nih.gov/nuccore/PQ844993.1/
datasets download virus genome accession ON634724.1 --filename ON634724_1.zip #Check on: https://www.ncbi.nlm.nih.gov/nuccore/2246546024

# the metadata of the sequence is on a .jsonl file
# this file contain a list of json objects on for each accession number.

unzip -o -q dengue_126437.zip -d dengue_126437
unzip -o -q PQ844993_1.zip -d PQ844993_1

# you can convert the jsonl file to a tsv file with the following command:
dataformat tsv virus-genome --inputfile dengue_126437/ncbi_dataset/data/data_report.jsonl >> dengue_126437.tsv
dataformat tsv virus-genome --inputfile PQ844993_1/ncbi_dataset/data/data_report.jsonl >> PQ844993_1.tsv
