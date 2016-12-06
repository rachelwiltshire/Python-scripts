# **Python-scripts**
This folder contains the Python scripts that I create whilst working towards my Ph.D in Medical Entomology (Population genetics of the malaria mosquito vectors *Anopheles gambiae* and *An. farauti*).

- #### MappedScaffs-MultipleSNPs4SNeP.py
Removes [unmapped scaffolds] and [mapped scaffolds with only one SNP] from the .map file to facilitate SNeP Ne analysis. SNeP errors out when it hits a 0 or has <2 SNPs to compare

- #### SCAFF2CHROM.py
Maps scaffolds in a .vcf file to chromosomes in the .agp file

- #### TrimmedReads-Pool2Individuals.py
Creates a fastq file of every individual's reads from a pooled demultiplexed file. I wrote this script because NCBI required each individual to have its own raw sequence files.
