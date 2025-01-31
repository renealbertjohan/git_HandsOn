#!/usr/bin/env python

# The packages and functions to be imported in python to succesfully execute this script
import sys, re
from argparse import ArgumentParser

# States the input arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") # Indicate your sequence
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif") # Indicate your motif you want to find in your sequence

# Exit the script if the input sequence has a length of equal to 1
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# This code checks first if there is a U in the sequence and then for A,T,G or C --> Simply reverted the if and elif and added |
# In addition, the code calculates and prints the percentage of each nucleotide, given a DNA or RNA sequence
args.seq = args.seq.upper() # Make all your letters in upper cases
if re.search('^[ACGTU]+$', args.seq):
    if re.search('U', args.seq):# Check if there is a U in your sequence (RNA) 
                                # Calculates the percentage for each nucleotide in your sequence 
        print ('The sequence is RNA','\n',
               'Nucleotide A content = ', round(args.seq.count("A") / len(args.seq) * 100, 2),'%','\n',
               'Nucleotide U content = ', round(args.seq.count("U") / len(args.seq) * 100, 2),'%','\n',
               'Nucleotide G content = ', round(args.seq.count("G") / len(args.seq) * 100, 2),'%','\n',
               'Nucleotide C content = ', round(args.seq.count("C") / len(args.seq) * 100, 2),'%', sep='')
    elif re.search('A|T|G|C', args.seq): # If not, it checks if there is a A, T, G or C in your sequence (DNA) 
                                         # Calculates the percentage for each nucleotide in your sequence  
        print ('The sequence is DNA','\n', 
               'Nucleotide A content = ', round(args.seq.count("A") / len(args.seq) * 100, 2),'%','\n',
               'Nucleotide T content = ', round(args.seq.count("T") / len(args.seq) * 100, 2),'%','\n',
               'Nucleotide G content = ', round(args.seq.count("G") / len(args.seq) * 100, 2),'%','\n',
               'Nucleotide C content = ', round(args.seq.count("C") / len(args.seq) * 100, 2),'%', sep='')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA') # If there are other letters then U, A, T, G and C in your sequence.

# Detects if there is a motif in the sequence (if provided)
if args.motif:
    args.motif = args.motif.upper() # Make all your letter in upper case
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("YES")
    else:
        print("NO")
