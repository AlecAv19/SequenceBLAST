# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:33:32 2025

@author: ASUS TUF F15
"""

#We use qblast from Bio.Blast for online Blast
from Bio import Blast
from Bio import SearchIO

#Email necessary for online Blast
Blast.tool
Blast.email = "A.N.Other@example.com"

#Open a sequence in FASTA format as a string and use it as the query argument 
fasta_string = open("sequence.fasta").read()

#Define the 3 main arguments for BLAST:
    #BLAST program for the search
    #Database for the search
    #String with the query sequence

result_stream = Blast.qblast("blastn", "nt", fasta_string)

#Save a copy of the output file
with open("my_blast.xml", "wb") as out_stream:
    out_stream.write(result_stream.read())

result_stream.close()

#Reopen the file to retreive the information for the data stream
result_stream = open("my_blast.xml", "rb")

#Show BLAST results
blast_qresult = SearchIO.read("my_blast.xml", "blast-xml")
print(blast_qresult)

#BLAST results lenght
len(blast_qresult)

#Show an specific hit. Example: Fourth hit
blast_hit = blast_qresult[3]
print(blast_hit)

#Show results for first hit and first HSP
blast_hsp = blast_qresult[0][0]
print(blast_hsp)
