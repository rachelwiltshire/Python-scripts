#!/usr/bin/python
#TRIMMOMATIC-AUTO.py#
#Author: Rachel Wiltshire, U. Notre Dame, January 2017
#Automated Trimmomatic usage for multiple samples - removes Illumina adapters and trims poor quality reads

#Usage: Give X <arguments> in addition to the script.py in this format:
        #TRIMMOMATIC-AUTO.py <input txt file> 

#This script is specifically for the WGS gDNA PE libraries AFar April 2013 sequenced on Illumina HiSeq2000 v.1.9
#Broad Institute (16 Anopheles genomes project)

#Import default system
import sys, gzip, glob, fileinput


#If no arguments were given, print helpful message
if len(sys.argv) != X:
        print "Error! Give X arguments.\nUsage: python TRIMMOMATIC-AUTO.py <txt>"
        sys.exit(0)

module load bio

inputdir = '~/FARAUTI/SRA_downloads'
outputdir = '~/FARAUTI/TERMINAL'

with gzip.open('/home/joe/file.txt.gz', 'rt') as f:
    file_content = f.read()
