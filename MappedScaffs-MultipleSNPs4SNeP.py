#!/usr/bin/python
#MappedScaffs-MultipleSNPs4SNeP.py
#Author: Rachel Wiltshire, U. Notre Dame, December 2016.
#Removes unmapped scaffolds and mapped scaffolds with only one SNP from the .map file to facilitate SNeP Ne analysis
## SNeP errors out when it hits a 0 or has <2 SNPs to compare

##Usage: Give 2 <arguments> in addition to the script.py in this format:
        #MappedScaffs-MultipleSNPs4SNeP.py <input map file> <output file>

##Import default system
import sys

##Print helpful message if no, or incorrect number of, arguments given
if len(sys.argv) != 3:
        print "Error! Give 2 arguments.\nUsage: python MappedScaffs-MultipleSNPs4SNeP.py <map> <outputfile>"
        sys.exit(0)

##Generate output file
oname = sys.argv[2] + "_mapped4SNeP.map"
out = open(oname, 'w')

##Read input map file and return records to the output file if they are 1) mapped, AND 2) occur more than once, on a scaffold  
map = open(sys.argv[1], 'r')
mlines = map.readlines()

## 1) Create chromosome dictionary 
chr_dict = {}

## 2) Loop through map file, add mapped scaffold/chromosomes (keys) to dictionary and count them (values)
for line in mlines:
        chr = line.strip().split('\t')[0]
        if chr != '0':
                if chr not in chr_dict:
                        chr_dict[chr] = 1
                else:
                        chr_dict[chr] += 1

## 3) Write chromosomes with at least two mapped SNPs to the output file
for line in mlines:
        chr = line.strip().split('\t')[0]
        if chr != '0' and chr_dict[chr] >= 2:
                out.write(line)

##Close output file
out.close()

##Close input file
map.close()

#END
