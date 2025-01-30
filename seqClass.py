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

args.seq = args.seq.upper() # Make all your letters in upper cases
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq): # Check if there is a T in your sequence
        print ('The sequence is DNA')
    elif re.search('U', args.seq):# Check if there is a U in your sequence
        print ('The sequence is RNA')
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
