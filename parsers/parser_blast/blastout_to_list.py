import argparse
import csv

def check_protein_presence(fasta_file, blast_file, output_file):
    protein_names = set()

    # Read the FASTA file and extract protein names
    with open(fasta_file, 'r') as fasta:
        for line in fasta:
            if line.startswith('>'):
                protein_name = line.strip()[1:]
                protein_names.add(protein_name)

    # Read the BLAST file into a list of lists
    blast_data = []
    with open(blast_file, 'r', newline='') as table:
        reader_blast = csv.reader(table, delimiter='\t')
        header = next(reader_blast)  # Skip the header line
        for row in reader_blast:
            blast_data.append(row)

    # Process the table file and write new table with presence information
    with open(output_file, 'w', newline='') as output:
        writer = csv.writer(output, delimiter='\t')

        # Write the header line with the new column
        header = ['protein_id', 'BLASTp', 'Homology_proteins']
        writer.writerow(header)

        # Iterate through each protein name in the FASTA file
        for protein_name in protein_names:
            found_proteins = []
            presence = 'no_homology'
            
            # Check if the protein is in the table and collect the found homology proteins
            for row in blast_data:
                if protein_name == row[0]:
                    found_proteins.append(row[1])
                    presence = 'homology'
            
            # Check if found_proteins is empty (i.e., no homologous proteins found)
            if not found_proteins:
                found_proteins = ['NA']
            
            # Write the row with the protein name, presence information, and found proteins
            writer.writerow([protein_name, presence, ','.join(found_proteins)])

    print(f"Protein presence has been checked and the new table is saved in '{output_file}'.")

# Create the argument parser
parser = argparse.ArgumentParser(description='Check protein presence in BLASTp output based on FASTA file.')

# Add the command-line arguments
parser.add_argument("-f","--fasta_file", help='Path to the FASTA file')
parser.add_argument("-b", "--blast_file", help='Path to the table file')
parser.add_argument("-o", "--output_file", help='Path to the output table file')

# Parse the command-line arguments
args = parser.parse_args()

# Call the function with the provided arguments
check_protein_presence(args.fasta_file, args.blast_file, args.output_file)