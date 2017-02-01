#!/usr/bin/python
#TRIMMOMATIC-AUTO.py#
#Author: Rachel Wiltshire, U. Notre Dame, January 2017
#Automated Trimmomatic usage for multiple samples - removes Illumina adapters and trims poor quality reads

#Usage: Give X <arguments> in addition to the script.py in this format:
        #TRIMMOMATIC-AUTO.py <input txt file> 

#This script is specifically for the WGS gDNA PE libraries AFar April 2013 sequenced on Illumina HiSeq2000 v.1.9
#Broad Institute (16 Anopheles genomes project)

#Import Python packages
import os, sys, gzip, glob, fileinput

#If no arguments were given, print helpful message
if len(sys.argv) != X:
        print "Error! Give X arguments.\nUsage: python TRIMMOMATIC-AUTO.py <txt>"
        sys.exit(0)

#Load bio program suite from CRC repository
module load bio

#Set variables
indir = '~/FARAUTI/SRA_downloads'
outdir = '~/FARAUTI/TERMINAL'

for filename in os.listdir(indir):
        if filename.endswith(.gz):
                with gzip.open('indir', 'rt') as f:
    file_content = f.read()

cd outdir
trimmomatic PE -threads 8 -phred33 -trimlog SRX277192_Tanna2_run1-SRR849988 \
SRX277192_Tanna2_run1-SRR849988-_1.fastq SRX277192_Tanna2_run1-SRR849988-_2.fastq \
SRX277192_Tanna2_run1-SRR849988-_1.paired.fq SRX277192_Tanna2_run1-SRR849988-_1.unpaired.fq \
SRX277192_Tanna2_run1-SRR849988-_2.paired.fq SRX277192_Tanna2_run1-SRR849988-_2.unpaired.fq \
ILLUMINACLIP:/afs/crc.nd.edu/user/r/rwiltshi/GROUP_SOLOMON/rwiltshi/AGam_chromosomes/TruSeq3-PE.fa:2:30:10 LEADING:5 TRAILING:5 SLIDINGWINDOW:4:15 MINLEN:50

cd indir
gzip SRX277192_Tanna2_run1-SRR849988-_*.fastq
