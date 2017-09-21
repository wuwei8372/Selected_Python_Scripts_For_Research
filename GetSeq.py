import csv
from Bio import SeqIO

idList = {}

with open ("NotFound.txt") as f:
    for line in f:
        res = line[0:len(line)-2]
        idList[res] = 1

print idList

for seq_record in SeqIO.parse("FinalDB.fasta","fasta"):
   # use hash structure to do fast search
    if (seq_record.description in idList):
            a = ">" + str(seq_record.description) + "\n" + str(seq_record.seq) + "\n" 
            print a
            res = open ("NotFound.fasta", "a")
            res.write(a)
