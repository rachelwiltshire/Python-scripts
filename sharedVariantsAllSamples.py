#!/usr/bin/python
#sharedVariantsAllSamples.py#
#Author: Rachel Wiltshire, February 2019

## generates .vcf file with variants that are present in ALL samples  ##

import sys

#Print helpful message if incorrect number of arguments given
if len(sys.argv) != 3:
        print 'Error! Give 2 arguments in the following format:\npython sharedVariantsAllSamples.py <vcf> <outfile>'
        sys.exit(1)

vcf = open(sys.argv[1], 'r')
out = open(sys.argv[2], 'w')

vline = vcf.readline()

while vline != "":
        if vline[0] == '#':
                out.write(vline)
        else:
                if "./." in vline:
                        vcf.readline()
                else:
                        out.write(vline)
        vline = vcf.readline()

vcf.close()
out.close()

#END
