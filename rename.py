#!/usr/bin/python
# rename.py #
# Author: Rachel Wiltshire, U. Notre Dame, February 2017 #
# A couple of useful scripts that replace characters and rename files globally #

#Usage: Call python rename.py

#These scripts are specifically for the WGS gDNA libraries AFar APril 2013 sequenced on Illumina HiSeq2000 v 1.9
#Broad Institute (16 Anopheles genomes project)
 
#Import dependencies
import os

#Define file type extensions to be included in global rename
SRA = (".fastq", ".fastq.gz")
trimmed = (".fq", ".fq.gz")
aligned = (".sai", ".sam")
picard = (".bai", ".bam", ".metrics.txt", ".metrics")
gatk = (".bai", ".bam", ".intervals", ".log", ".vcf", ".vcf.idx")

#Replace an unwanted character with another
for filename in os.listdir("."):              # . signifies the cwd -change this if you are working elsewhere
        if filename.endswith(tuple(aligned)):
                os.rename(filename, filename.replace("-", "_"))
                print filename

#Get filenames defined in global rename and rename
for filename in os.listdir("."):
        if filename.endswith(tuple(aligned)): #(aligned) is just an example here - can use any tuple as defined above                                       
                print filename
                fparts = filename.rsplit('_',1)
                print fparts
                newfilename = fparts[0] + fparts[1]
                print newfilename               
                os.rename(filename, newfilename)
                print filename + " > " + newfilename

#END
