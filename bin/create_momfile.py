import sys

def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            # Skip empty lines
            if not line.strip():
                continue
            
            # Split the line into components
            parts = line.split()
            index = parts[0]
            value = float(parts[1])
            
            # Write the formatted line to the output file
            outfile.write(f"{index:2}  1   {value:10.6f}   0.0000000   0.0000000   1.0000000\n")

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_filename> <output_filename>")
        sys.exit(1)
    

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    process_file(input_filename, output_filename)
    print(f"Processed data has been written to {output_filename}.")

if __name__ == "__main__":
    main()

