#!/usr/bin/python
#TRIMMOMATIC-AUTO.py#
#Author: Rachel Wiltshire, U. Notre Dame, January 2017
#Automated Trimmomatic usage for multiple samples - removes Illumina adapters and trims poor quality reads

#Usage: Call python and TRIMMOMATIC-AUTO.py

#This script is specifically for the WGS gDNA PE libraries AFar April 2013 sequenced on Illumina HiSeq2000 v.1.9
#Broad Institute (16 Anopheles genomes project)

#Import Python packages
import os, gzip, subprocess

#Set variables
indir = '~/FARAUTI/SRA_downloads'
outdir = '~/FARAUTI/TERMINAL'
trimmomatic = '/opt/crc/bio/Trimmomatic'
illclip = 'ILLUMINACLIP:/afs/crc.nd.edu/user/r/rwiltshi/GROUP_SOLOMON/rwiltshi/AGam_chromosomes/TruSeq3-PE.fa:2:30:10'
lead = 'LEADING:5'
trail = 'TRAILING:5'
slide = 'SLIDINGWINDOW:4:15'
minlen = 'MINLEN:50'

for filename in os.listdir(indir):
        if filename.endswith("_1.fastq.gz"):
                f1 = filename
        elif filename.endswith("_2.fastq.gz"):
                f2 = filename

                with gzip.open('f1', 'rt', 'wt') and gzip.open('f2', 'rt', 'wt') as f:
                        f1parts = f1.split("_")
                        f1paired = f1parts[0:2] + "_1.paired.fq"
                        f1unpaired = f1parts[0:2] + "_1.unpaired.fq"
                        f2parts = f2.split("_")
                        f2paired = f2parts[0:2] + "_2.paired.fq"
                        f2unpaired = f2parts[0:2] + "_2.unpaired.fq"
                        trimlog = f1parts[0:2]
                        cd outdir
        
                        subprocess.call(['trimmomatic', 'PE', '-threads 8', '-phred33', '-trimlog', 'f1', 'f2', 'f1paired', 'f1unpaired', 'f2paired', 'f2unpaired', 'illclip', 'lead', 'trail', 'slide', 'minlen'])
PE -threads 8 -phred33 -trimlog filename \
SRX277192_Tanna2_run1-SRR849988-_1.fastq SRX277192_Tanna2_run1-SRR849988-_2.fastq \
SRX277192_Tanna2_run1-SRR849988-_1.paired.fq SRX277192_Tanna2_run1-SRR849988-_1.unpaired.fq \
SRX277192_Tanna2_run1-SRR849988-_2.paired.fq SRX277192_Tanna2_run1-SRR849988-_2.unpaired.fq \
ILLUMINACLIP:/afs/crc.nd.edu/user/r/rwiltshi/GROUP_SOLOMON/rwiltshi/AGam_chromosomes/TruSeq3-PE.fa:2:30:10 LEADING:5 TRAILING:5 SLIDINGWINDOW:4:15 MINLEN:50
else: continue
