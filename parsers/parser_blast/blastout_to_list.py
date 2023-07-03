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

    # Process the table file and write new table with presence information
    with open(blast_file, 'r', newline='') as table, open(output_file, 'w', newline='') as output:
        reader_blast = csv.reader(table, delimiter='\t')
        writer = csv.writer(output, delimiter='\t')

         # Skip the header line
        next(reader_blast)

        # Extract the protein names from the first column of the table file
        table_protein_names = [row[0] for row in reader_blast]

        # Reset the file pointer to the beginning of the table file
        table.seek(0)

        # Write the header line
        header = ['protein_id', 'BLASTp']
        writer.writerow(header)

        # Iterate through each protein name in the FASTA file
        for protein_name in protein_names:
            presence = 'homology' if protein_name in table_protein_names else 'no_homology'
            writer.writerow([protein_name, presence])

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