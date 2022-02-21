# **Python-scripts**
This folder contains the Python scripts that I create whilst working towards my Ph.D in Medical Entomology (Population genetics of the malaria mosquito vectors *Anopheles gambiae* and *An. farauti*).

- #### BWA-AUTO.py
The second step in my WGS processing pipeline. Automates the *BWA* shell script, which aligns reads to the reference genome to generate a SAM file.

- #### MappedScaffs-MultipleSNPs4SNeP.py
Removes [unmapped scaffolds] and [mapped scaffolds with only one SNP] from the .map file to facilitate *SNeP* Ne analysis. *SNeP* errors out when it hits a 0 or has <2 SNPs to compare

- #### mozGoldenPathDmel.py
Creates multiple alignments (.maf) containing selected mosquito seqs. aligned to Drosophila melanogaster dm6.chr assemblies (http://hgdownload.soe.ucsc.edu/goldenPath/dm6/multiz124way/maf/) for further evolutionary inference.

- #### SCAFF2CHROM.py
Maps scaffolds in a .vcf file to chromosomes in the .agp file

- #### TrimmedReads-Pool2Individuals.py
Creates a fastq file of every individual's reads from a pooled demultiplexed file. I wrote this script because NCBI required each individual to have its own raw sequence files.

- #### TRIMMOMATIC-AUTO.py
The first step in my WGS processing pipeline. Automates the *trimmomatic* shell script, which trims Illumina sequencing and other adapters from the reads.
