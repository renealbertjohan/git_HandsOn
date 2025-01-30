#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") # Indicate your sequence
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif") # Indicate your motif you want to find in your sequence

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()


# The code checks first if there is a U in the sequence and then for A,T,G or C --> Simply reverted the if and elif and added |
args.seq = args.seq.upper() # Make all your letters in upper cases
if re.search('^[ACGTU]+$', args.seq):
    if re.search('U', args.seq):# Check if there is a U in your sequence
        print ('The sequence is RNA')
    elif re.search('A|T|G|C', args.seq): # Check if there is a A, T, G or C in your sequence
        print ('The sequence is DNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

if args.motif:
    args.motif = args.motif.upper() # Make all your letter in upper case
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("YES")
    else:
        print("NO")
