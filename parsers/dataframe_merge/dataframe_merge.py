import argparse
import pandas as pd

def merge_tsv_files(input_files, output_file):
    dfs = []
    
    for file in input_files:
        df = pd.read_csv(file, sep='\t', quotechar="'")
        dfs.append(df)

    df = dfs[0]
    for i in range(1, len(dfs)):
        df = df.merge(dfs[i], on='protein_id')
    
    print("Merged DataFrame:")
    print(df.head())  # Print the first few rows of the merged DataFrame for verification
    
    df.to_csv(output_file, sep='\t', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merge TSV files.')
    parser.add_argument('-i','--input_files', nargs='+', help='Input TSV files to merge')
    parser.add_argument('-o','--output_file', help='Output TSV file')
    args = parser.parse_args()

    merge_tsv_files(args.input_files, args.output_file)


# Additional code to check the data type of the 'protein_id' column in each input file
    for file in args.input_files:
        df = pd.read_csv(file, sep='\t', quotechar="'")
        protein_id_data_type = df['protein_id'].dtype
        print(f"Data type of 'protein_id' column in {file}: {protein_id_data_type}")