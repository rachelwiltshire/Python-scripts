#!/usr/bin/python
#TrimmedReads-Pool2Individuals.py
#Author: Rachel Wiltshire (U. Notre Dam) October 2016
#Creates individual fasta files containing trimmed reads (from trimmer.py processing) specific to IDs from pooled FWD and REV files

#Usage: Give 2 <arguments> in addition to the script.py in this format:
        #TrimmedReads-Pool2Individuals.py <input txt file> <input fasta file>

#Import default system
import sys

#If no arguments were given, print helpful message
if len(sys.argv) != 3:
        print "Error! Give 2 arguments.\nUsage: python TrimmedReads-Pool2Individuals.py <txt> <fasta>"
        sys.exit(0)

txt = open(sys.argv[1])
fst = open(sys.argv[2])

#Get fasta file name
fparts = sys.argv[2].split("_")
fname = fparts[2] 

#If input fasta file has a 1 in the name i.e. RMW_RAD_1.pe.trimmed.fq then it is a FWD read file (2 = REV) and this should be appended to the outfile name
if fname[0] == "1":                                             #Starts with 1 (fname is now fparts[2] = 1.pe.trimmed.fq)
        fname = "FWD" + fname[1:]                               #Change 1 to FWD
else:
        fname = "REV" + fname[1:]                               #Change 2 to REV

tline = txt.readline().strip()
fline = fst.readline()

#Loop through fasta file with regex and return a record (ID line + trailing 3 lines) to the outfilename for each hit
#Upon completion, return to next ID in txt file and repeat loop until all IDs in txt file have been looped through

while tline != "":
        ID = tline.split("\t")[0]                               #Split txt file by tabs and take the first column (Python = 0 count)
        outfilename = "PRJNA344468_" + ID + "_" + fname         #Generate an output file for each ID result     
        outfile = open(outfilename, 'w')        
        while fline != "":
                seq = fst.readline()                            #First trailing line i.e. AGCTCTCTGATCG
                info = fst.readline()                           #Second trailing line i.e. +
                qual = fst.readline()                           #Third trailing line i.e. bbbccchhiizsd 
                if ID in fline:
                        outfile.write(fline + seq + info + qual)
                fline = fst.readline()
        outfile.close() 
        tline = txt.readline().strip()
        fst.seek(0)             
        fline = fst.readline()

#Close input files
txt.close()
fst.close()

#END
