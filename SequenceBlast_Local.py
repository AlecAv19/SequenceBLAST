# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 13:16:22 2025

@author: ASUS TUF F15
"""

from Bio import Blast
import subprocess

# Define input parameters for the database creation
fasta_file = "Model_organisms.fasta"
db_name = "Model_organisms"
db_title = "Model_DB"
db_type = "nucl"
test_file = "sequence.fasta"

# Construct the makeblastdb with a FASTA file containing model organisms sequences
cmd = [
    "makeblastdb",
    "-in", fasta_file,
    "-dbtype", db_type,
    "-parse_seqids",
    "-out", db_name,
    "-title", db_title
]

# Run and check for errors in the database creation
try:
    subprocess.run(cmd, check=True)
    print(f"BLAST database '{db_name}' created successfully with title '{db_title}'.")
except subprocess.CalledProcessError as e:
    print(f"Error during BLAST database creation: {e}")
except FileNotFoundError:
    print("Error: makeblastdb command not found. Ensure BLAST+ is installed and available in PATH.")

# Run BLAST search
cmd = [
    "blastn",
    "-query", test_file,
    "-db", db_name,
    "-out", "Model_organisms.xml",
    "-evalue", "0.001",
    "-outfmt", "5"
]

try:
    subprocess.run(cmd, check=True)
    print("BLAST search completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error during BLAST search: {e}")

# Parse BLAST results and print them
try:
    with Blast.parse("Model_organisms.xml") as blast_records:
        for record in blast_records:
            print(f"Query: {record.query}")
            for alignment in record.alignments:
                print(f"Best hit: {alignment.title}")
                for hsp in alignment.hsps:
                    print(f"Score: {hsp.score}")
                    print(f"E-value: {hsp.expect}")
                    print("-" * 50)
except Exception as e:
    print(f"Error parsing the BLAST results: {e}")