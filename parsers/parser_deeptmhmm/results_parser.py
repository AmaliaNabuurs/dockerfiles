import csv
import argparse

# Add parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file", help="input file path", required=True)
parser.add_argument("-o", "--output_file", help="output file path", required=True)
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file

with open(input_file, 'r') as file:
    lines = file.readlines()

names_positions = []
for line in lines:
    if line.startswith(">"):
        line = line.strip()
        name, position = line.split(" | ")
        names_positions.append((name[1:], position))

# Write to TSV file with headers
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(["protein_id", "DeepTMHMM_prediction"])  # Write header row
    writer.writerows(names_positions)  # Write data rows