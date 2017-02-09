#!/usr/bin/python
#BWA-AUTO.py#
#Author: Rachel Wiltshire, U. Notre Dame, February 2017
#Automated BWA usage for multiple samples - alignment of reads to reference genome

#Usage: Call python and BWA-AUTO.py

#This script is specifically for the WGS gDNA PE libraries AFar April 2013 sequenced on Illumina HiSeq2000 v.1.9
#Broad Institute (16 Anopheles genomes project)

#Import Python packages
import os, gzip, subprocess

#Set variables
indir = '/afs/crc.nd.edu/user/r/rwiltshi/FARAUTI/TERMINAL/trimmed/'
outdir = '/afs/crc.nd.edu/user/r/rwiltshi/FARAUTI/TERMINAL/aligned/'
bwa = '/opt/crc/bio/BWA/0.6.2/bin/bwa'    #v.0.6.2 is recommended for aln/sampe/samse #v.0.7.12 for mem
samtools = '/opt/crc/bio/samtools/1.2.231.0/bin/samtools'
AfarRef = '/afs/crc.nd.edu/user/r/rwiltshi/FARAUTI/Anopheles-farauti-FAR1_SCAFFOLDS_AfarF2.fa'

space = " "
f1 = ""
f2 = ""

#Index the reference genome file
bwaindexCMD = bwa + " index " + space + AfarRef
print bwaindexCMD
subprocess.call(bwaindexCMD, shell=True)

#generate the fasta file index >> creates a file ref.fa.fai, with one record/line for each of the contigs in the ref.fa file
samtoolsCMD = samtools + " faidx " + space + AfarRef
print samtoolsCMD
subprocess.call(samtoolsCMD, shell=True)

#Run through data files in directory and execute shell command when conditions are met
#indir MUST be sorted first as os.listdir() is in arbitrary order as an artifact of the filesystem
for filename in sorted(os.listdir(indir)):      
        #print filename
        #continue
        
        if filename.endswith("_1.fastq"):
                f1 = filename
        elif filename.endswith("_2.fastq"):
                f2 = filename
        else:
                continue

        if ((f1 != "" and f2 != "") and (f1[0:-11] == f2[0:-11])):
                with gzip.open(f1) as f, gzip.open(f2) as g:
                        f1parts = f.name.rsplit("_", 1)
                        f1paired = f1parts[0] + "_1.paired.fq"
                        f1unpaired = f1parts[0] + "_1.unpaired.fq"
                        f2parts = g.name.rsplit("_", 1)
                        f2paired = f2parts[0] + "_2.paired.fq"
                        f2unpaired = f2parts[0] + "_2.unpaired.fq"
                
                        bwaalnCMD = bwa + " PE -threads 8 -phred33 " + " " + f1 + " " + f2 + " " + outdir + f1paired + \
                                        " " + outdir + f1unpaired + " " + outdir + f2paired + " " + outdir + f2unpaired + \
                        
                        print bwaalnCMD
                        subprocess.call(bwaalnCMD, shell=True)
                        f1 = ""
                        f2 = ""

#END

#generate intermediate .sai files by aligning paired reads to reference genome
bwa aln -t 12 -q 5 -l 32 -k 3 -n 9 -o 1 AfarRef SRX277192_Tanna2_run1-SRR849988-_1.paired.fq \
> SRX277192_Tanna2_run1-SRR849988-_1.pe.aligned.sai
bwa aln -t 12 -q 5 -l 32 -k 3 -n 9 -o 1 AfarRef SRX277192_Tanna2_run1-SRR849988-_2.paired.fq \
> SRX277192_Tanna2_run1-SRR849988-_2.pe.aligned.sai

#generate .sam file
bwasamCMD = bwa + " sampe " + space + AfarRef \
SRX277192_Tanna2_run1-SRR849988-_1.pe.aligned.sai SRX277192_Tanna2_run1-SRR849988-_2.pe.aligned.sai \
SRX277192_Tanna2_run1-SRR849988-_1.paired.fq SRX277192_Tanna2_run1-SRR849988-_2.paired.fq \
> SRX277192_Tanna2_run1-SRR849988.pe.aligned.sam

#END
