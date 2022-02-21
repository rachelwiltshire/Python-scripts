#!/usr/bin/python
#mozGoldenPathDmel.py
#Author: Rachel Wiltshire, U. Notre Dame, June 2021
#Creates multiple alignments (.maf) containing selected mosquito seqs. aligned to Drosophila melanogaster dm6.chr assemblies

#Usage: Give 1 <argument> in addition to the script.py in this format:
#python mozGoldenPathDmel.py <chr.maf>

import sys

if len(sys.argv) !=2:
    print ("Error! Give 1 argument.\nUsage: python mozGoldenPathDmel.py <chr.maf>")
    sys.exit(0)

maf = open(sys.argv[1], 'r')
mname = sys.argv[1]
mline = maf.readline()
moz_of_interest = ["aegypti", "quinquefasciatus", "epiroticus", "farauti", "farauti_No4", "gambiae", "koliensis",
 "punctulatus"]
outfilename = "moz" + mname
outfile = open(outfilename, 'w')

if mline[0] == "#":
    outfile.write(mline)
    mline = maf.readline()
written = 0

while mline != "":
    info_to_write = ""
    if mline[0] == 'a':
        info_to_write += mline
        info_to_write += maf.readline()
        mline = maf.readline()
        moz_to_write = ""
        
        while mline.strip() != "":
            for moz in moz_of_interest:
                if moz in mline:
                    moz_to_write += mline
                    break
            mline = maf.readline()
        
        if moz_to_write != "":
            outfile.write(info_to_write + moz_to_write + "\n")
            written += 1
            
            if written % 1000 == 0:
                print("Written " + str(written) + " scored regions")
    mline = maf.readline()

outfile.close()
maf.close()
#END
