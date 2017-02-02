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
indir = '/afs/crc.nd.edu/user/r/rwiltshi/FARAUTI/SRA_downloads/test'
outdir = '/afs/crc.nd.edu/user/r/rwiltshi/FARAUTI/TERMINAL/'
trimmomatic = '/opt/crc/bio/Trimmomatic/0.32/bin/trimmomatic'
illclip = 'ILLUMINACLIP:/afs/crc.nd.edu/user/r/rwiltshi/GROUP_SOLOMON/rwiltshi/AGam_chromosomes/TruSeq3-PE.fa:2:30:10'
lead = 'LEADING:5'
trail = 'TRAILING:5'
slide = 'SLIDINGWINDOW:4:15'
minlen = 'MINLEN:50'

f1 = ""
f2 = ""

#Read through files in input directory and find matching pair (SRX_AND_RUN_1.fastq.gz and SRX_AND_RUN_2.fastq.gz)
for filename in os.listdir(indir):
        if filename.endswith("_1.fastq.gz"):
                f1 = filename
        elif filename.endswith("_2.fastq.gz"):
                f2 = filename
        else:
                continue
        
        #If you've found a matching file pair that both have content, unzip them and set variables
        if ((f1 != "" and f2 != "") and (f1[0:-11] == f2[0:-11])):      
                with gzip.open(f1) as f, gzip.open(f2) as g:
                        f1parts = f.name.rsplit("_", 1)
                        f1paired = f1parts[0] + "_1.paired.fq"
                        f1unpaired = f1parts[0] + "_1.unpaired.fq"
                        f2parts = g.name.rsplit("_", 1)
                        f2paired = f2parts[0] + "_2.paired.fq"
                        f2unpaired = f2parts[0] + "_2.unpaired.fq"
                        trimlog = f1parts[0] + ".trimlog"
                
                        #Define trimmomatic parameters
                        trimmomaticCMD = trimmomatic + " PE -threads 8 -phred33 -trimlog " + trimlog + " " + f1 + " " + f2 + \
                                + " " + outdir + f1paired + " " + outdir + f1unpaired + " " + outdir + f2paired + " " + \
                                outdir + f2unpaired + " " + illclip + " " + lead + " " + trail + " " + slide + " " + minlen
                        
                        print trimmomaticCMD
                        
                        #Call the command in the Python script and set it to execute through the shell
                        subprocess.call(trimmomaticCMD, shell=True)
                        f1 = ""
                        f2 = ""

#END
