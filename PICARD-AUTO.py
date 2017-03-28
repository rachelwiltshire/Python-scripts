#!/usr/bin/python
# PICARD-AUTO.py #
# Author: Rachel Wiltshire, U. Notre Dame, February 2017 #
# Automated pre-processing of reads prior to variant calling with GATK #

#Usage: Call python, PICARD-AUTO.py and ReadGroupInfo.txt (also, filename arguments if processing a range in a sorted directory list)
        #i.e. python PICARD-AUTO.py < ReadGroupInfo.txt > (< file.sam >)

#This script is specifically for the WGS gDNA PE libraries AFar April 2013 sequenced on Illumina HiSeq2000 v1.9
#Broad Institute (16 Anopheles genomes project)

#Import dependencies
import os, pprint, subprocess, sys
#print sys.argv[2]
#sys.exit(0)

#Print helpful message if incorrect number of arguments given
if len(sys.argv) < 2:
        print 'Error! Give at least 2 arguments in the following format:\npython PICARD-AUTO.py ReadGroupInfo.txt (< file.sam > if processing a range of files)'
        sys.exit(1)
        
#Set variables and logic statements
if len(sys.argv) > 3:           #If a file.sam argument is given
        processall = False      #Do not process until filename in sorted(os.listdir(indir)) = sys.argv[2]
else:
        processall = True       #Process filename as per the FOR loop
#print processall
#sys.exit(0)

indir = '/afs/crc.nd.edu/user/r/rwiltshi/FARAUTI/TERMINAL/aligned/PICTEST'
outdir = '/afs/crc/nd.edu/user/r/rwiltshi/FARAUTI/TERMINAL/picard/PICTEST'
picard = '/opt/crc/bio/picardtools/1.119/bin/'
VAL = "VALIDATION_STRINGENCY=LENIENT"
INDEX = "CREATE_INDEX=TRUE"
COORD = "SO=coordinate"
AfarRef = '/afs/crc.nd.edu/user/r/rwiltshi/FARAUTI/TERMINAL/trimmed/Anopheles-farauti-FAR1_SCAFFOLDS_AfarF2.fa'
space = " "
sam = ""                        #initializing variable to zero length string
dict = "Anopheles-farauti-FAR1_SCAFFOLDS_AfarF2.dict"

#Create a sequence dictionary that reads fasta or fasta.gz files containing reference sequences, and writes them as a .sam file
#picardseqdictCMD = picard + "CreateSequenceDictionary" + " REFERENCE=" + AfarRef + " OUTPUT=" + dict
#print picardseqdictCMD
#subprocess.call(picardseqdictCMD, shell=True)

#Run through filenames in directory and execute shell command when conditions are met
#indir MUST be sorted first as os.listdir() is in arbitrary order as an artifact of the filesystem
for filename in sorted(os.listdir(indir)):
        if filename.endswith("_.pe.aligned.sam"):
                sam = filename
        else:
                continue

        if (len(sys.argv) > 2 and sys.argv[2] == filename) or processall == True:
                if processall == False:
                        processall = True
        else:
                continue
        #print filename                 #output: SRX277xxx_Name_runx_SRR8xxxxx_.pe.aligned.sam
        #continue

        with open(sam) as f:
                fparts = f.name.rsplit('_',1)
                print fparts            #output: ['SRX277xxx_Name_runx_SRR8xxxxx', '.pe.aligned.sam']
                #print fparts[0]        #output: SRX277xxx_Name_runx_SRR8xxxxx
                #print fparts[1]        #output: .pe.aligned.sam
                #continue
                #sys.exit(0)


                clean = fparts[0] + ".clean.sam"
                readgroup = fparts[0] + ".rdgrp.sam"
                sorted = fparts[0] + ".sorted.bam"
                aln_metrics = fparts[0] + ".aln.sorted.metrics.txt"
                marked = fparts[0] + ".dedup.bam"
                dedup_metrics = fparts[0] + ".dedup.metrics.txt"

#Clean the alignment - soft clip any reads that extend beyond the edge of an assembly - reads are marked as MapQ0
        #picardcleanCMD = picard + "CleanSam" + " INPUT=" + sam + " OUTPUT=" + clean + space + VAL
        #print picardcleanCMD
        #subprocess.call(picardcleanCMD, shell=True)

#Add or replace read groups in an input .sam file to allow merging multiple .bam files (GATK does not support .sam files without headers)
        txt = sys.argv[1]
        print txt               
        with open(txt) as t:
                for tline in t:
                        if tline.startswith("#"):
                                continue
                        elif tline != "":
                                tparts = tline.strip().split('\t')
                                INDV = tparts[0]
                                RUN = tparts[1]
                                RGID = tparts[2]
                                RGLB = tparts[3]
                                RGPL = tparts[4]
                                RGPU = tparts[5]
                                RGSM = tparts[6]                        
                                #pprint.pprint(tparts)
                        
                                #picardreadgroupsCMD = picard + "AddOrReplaceReadGroups" + " INPUT=" + clean + " OUTPUT=" + readgroup \
                                #+ space + INDEX + space + COORD + " RGID=" + RGID + " RGLB=" + RGLB + " RGPL=" + RGPL + " RGPU=" \
                                #+ RGPU + " RGSM=" + RGSM + space + VAL

                                #if fparts[0].find(RUN) > -1:
                                        #print "found " + RUN + " in " + fparts[0]
                                        #pprint.pprint(picardreadgroupsCMD)
                                        #subprocess.call(picardreadgroupsCMD, shell=True)
                                #else:
                                        #continue

#Sort by reference - sort reads into .bam files based on the reference assembly to which they were mapped
        #picardsortsamCMD = picard + "SortSam" + " INPUT=" + readgroup + " OUTPUT=" + sorted + space + COORD + space + VAL
        #print picardsortsamCMD
        #subprocess.call(picardsortsamCMD, shell=True)

#Collect alignment summary metrics - details quality of read alignments and proportion of reads passing machine signal-to-noise threshold quality filters
        picardalnmetricsCMD = picard + "CollectAlignmentSummaryMetrics" + " REFERENCE_SEQUENCE=" + AfarRef + " INPUT=" + sorted \
                                + " OUTPUT=" + aln_metrics + " ASSUME_SORTED=true " + VAL
        print picardalnmetricsCMD
        subprocess.call(picardalnmetricsCMD, shell=True)

#Matches all read pairs with identical 5' coordinates and mapping orientations and marks as duplicates all but the best read pair (highest sum of base qualities where Q >=15)
        #picardmarkCMD = picard + "MarkDuplicates" + " INPUT=" + sorted + " OUTPUT=" + marked + space + INDEX + " METRICS_FILE=" \
                                #+ dedup_metrics + space + VAL
        #print picardmarkCMD
        #subprocess.call(picardmarkCMD, shell=True)

#Index coordinate-sorted .bam file for variant calling in GATK
        #picardbamindexCMD = picard + "BuildBamIndex" + " INPUT=" + marked + space + VAL
        #print picardbamindexCMD
        #subprocess.call(picardbamindexCMD, shell=True)

#END
