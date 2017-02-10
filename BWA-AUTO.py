#!/usr/bin/python
#BWA-AUTO.py#
#Author: Rachel Wiltshire, U. Notre Dame, February 2017
#Automated BWA usage for multiple samples - alignment of reads to reference genome

#Usage: Call python and BWA-AUTO.py

#This script is specifically for the WGS gDNA PE libraries AFar April 2013 sequenced on Illumina HiSeq2000 v.1.9
#Broad Institute (16 Anopheles genomes project)

#Import Python packages
import os, subprocess

#Set variables
indir = '/afs/crc.nd.edu/user/r/rwiltshi/FARAUTI/TERMINAL/trimmed/'
outdir = '/afs/crc.nd.edu/user/r/rwiltshi/FARAUTI/TERMINAL/aligned/'
bwa = '/opt/crc/bio/BWA/0.6.2/bin/bwa'    #v.0.6.2 is recommended for aln/sampe/samse #v.0.7.12 for mem
samtools = '/opt/crc/bio/samtools/1.2.231.0/bin/samtools'
AfarRef = '/afs/crc.nd.edu/user/r/rwiltshi/FARAUTI/TERMINAL/trimmed/Anopheles-farauti-FAR1_SCAFFOLDS_AfarF2.fa'

space = " "
f1paired = ""
f2paired = ""

#Index the reference genome file
bwaindexCMD = bwa + " index" + space + AfarRef
print bwaindexCMD
subprocess.call(bwaindexCMD, shell=True)

#generate the fasta file index >> creates a file ref.fa.fai, with one record/line for each of the contigs in the ref.fa file
samtoolsCMD = samtools + " faidx" + space + AfarRef
print samtoolsCMD
subprocess.call(samtoolsCMD, shell=True)

#Run through data files in directory and execute shell command when conditions are met
#indir MUST be sorted first as os.listdir() is in arbitrary order as an artifact of the filesystem
for filename in sorted(os.listdir(indir)):      
        #print filename
        #continue
        
        if filename.endswith("_1.paired.fq"):
                f1paired = filename
        elif filename.endswith("_2.paired.fq"):
                f2paired = filename
        else:
                continue

        if ((f1paired != "" and f2paired != "") and (f1paired[0:-11] == f2paired[0:-11])):
                with open(f1paired) as f, open(f2paired) as g:
                        f1parts = f.name.rsplit("_", 1)
                        f1sai = f1parts[0] + "_1.pe.aligned.sai"
                        f2parts = g.name.rsplit("_", 1)
                        f2sai = f2parts[0] + "_2.pe.aligned.sai"
                        sam = f1parts[0] + ".pe.aligned.sam"
                
                        #generate intermediate .sai files by aligning paired reads to reference genome
                        bwaalnCMD1 = bwa + " aln -t 12 -q 5 -l 32 -k 3 -n 9 -o 1" + space + AfarRef + space + f1paired + " >" + space + outdir + f1sai
                        
                        print bwaalnCMD1
                        
                        bwaalnCMD2 = bwa + " aln -t 12 -q 5 -l 32 -k 3 -n 9 -o 1" + space + AfarRef + space + f2paired + " >" + space + outdir + f2sai
                        
                        print bwaalnCMD2
                        
                        subprocess.call(bwaalnCMD1, shell=True)
                        
                        subprocess.call(bwaalnCMD2, shell=True)

                        #generate .sam file
                        bwasamCMD = bwa + " sampe" + space + AfarRef + space + outdir + f1sai + space + outdir + f2sai + \
                        indir + f1paired + indir + f2paired + " >" + space + outdir + sam
                        
                        print bwasamCMD
                        
                        subprocess.call(bwasamCMD, shell=True)
                        
                        f1paired = ""
                        f2paired = ""
                        
#END

#shell script
#generate intermediate .sai files by aligning paired reads to reference genome
bwa aln -t 12 -q 5 -l 32 -k 3 -n 9 -o 1 AfarRef SRX277192_Tanna2_run1-SRR849988-_1.paired.fq \
> SRX277192_Tanna2_run1-SRR849988-_1.pe.aligned.sai
bwa aln -t 12 -q 5 -l 32 -k 3 -n 9 -o 1 AfarRef SRX277192_Tanna2_run1-SRR849988-_2.paired.fq \
> SRX277192_Tanna2_run1-SRR849988-_2.pe.aligned.sai
#generate .sam file
SRX277192_Tanna2_run1-SRR849988-_1.pe.aligned.sai SRX277192_Tanna2_run1-SRR849988-_2.pe.aligned.sai \
SRX277192_Tanna2_run1-SRR849988-_1.paired.fq SRX277192_Tanna2_run1-SRR849988-_2.paired.fq \
> SRX277192_Tanna2_run1-SRR849988.pe.aligned.sam
#END
