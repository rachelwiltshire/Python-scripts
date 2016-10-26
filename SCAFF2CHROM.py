#!/usr/bin/python

#Author: Lauren Assour
#Modified by Rachel Wiltshire, U. Notre Dame, 2015.

## matches AGam scaffolds in the vcf file to AGam chromosomes in the agp file ##

import sys

#Print helpful message if incorrect number of arguments given
if len(sys.argv) != 4:
    print 'Error! Give 3 arguments in the following format:\npython SCAFF2CHROM.py <agp> <vcf> <outputfile>'
    sys.exit(1)

agp = open(sys.argv[1])
vcf = open(sys.argv[2])
out = open(sys.argv[3], 'w')

aline = agp.readline()
vline = vcf.readline()

astuff = {}

while aline != "":
    parts = aline.split()
    astuff[parts[5]] = 0
    aline = agp.readline()

agp.close()

print astuff

while vline != "":
    if vline[0] == '#':
        out.write(vline)

    vparts = vline.split()

    if vparts[0] in astuff:
        out.write(vline)
    
    vline = vcf.readline()

vcf.close()

#END
