import sys


def process_file_with_range(input_filename, output_filename, start_line, end_line, new_value):
    """
    Reads an input file, updates a range of lines with a specified value in the third column, 
    and writes the modified content to an output file.

    :param input_filename: The name of the input file to read.
    :param output_filename: The name of the output file to write.
    :param start_line: The starting line number (1-based index) of the range to update.
    :param end_line: The ending line number (inclusive, 1-based index) of the range to update.
    :param new_value: The new value to set for the third column in the specified range.
    """
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line_number, line in enumerate(infile, start=1):
            # Split the line into components
            parts = line.split()

            if not parts or len(parts) < 6:
                raise ValueError(
                    f"Invalid line format at line {line_number}: {line}")

            # Update the third column if the line number is in the specified range
            if start_line <= line_number <= end_line:
                # Update the third column within the range
                parts[2] = f"{new_value:.3f}"
            else:
                parts[2] = "0.000"  # Set third column to 0.000 for other lines

            # Format and write the output line
            formatted_line = (
                f"{int(parts[0]):2}  {int(parts[1]):1}   {float(parts[2]):6.3f}   "
                f"{float(parts[3]):6.3f}    0.0  0.0  1.0   0.0\n"
            )
            outfile.write(formatted_line)

    print(f"Processed file written to {output_filename}")


# Example Usage
input_file = "momfile_clus"  # Replace with the actual input filename
output_file = "kfile_clus"  # Replace with the desired output filename

if int(sys.argv[1]) == 0:
    start_line = 1  # Starting line number for the range
    end_line = 19  # Ending line number for the range
elif int(sys.argv[1]) == 1:
    start_line = 21  # Starting line number for the range
    end_line = 38  # Ending line number for the range
else:
    print("Argument should be 0 or 1")

new_value = -0.030  # The value to set for the third column in the range

process_file_with_range(input_file, output_file,
                        start_line, end_line, new_value)


def write_data(filename, flag):
    """
    Writes data to a file based on the value of the flag.

    :param filename: Name of the output file
    :param flag: Determines the pattern of data to write (1 or 0)
    """
    with open(filename, 'w') as file:
        if flag == 0:
            file.write(f" 1  1   -0.030   0.000    0.0  0.0  1.0   0.0\n")
        elif flag == 1:
            # Write reduced dataset
            file.write(f" 1  1   -0.000   0.000    0.0  0.0  1.0   0.0\n")
            file.write(f" 2  1   -0.030   0.000    0.0  0.0  1.0   0.0\n")
            file.write(f" 3  1   -0.000   0.000    0.0  0.0  1.0   0.0\n")
        else:
            raise ValueError("Flag must be either 0 or 1.")
    print(f"Data has been written to {filename}.")


output_filename = "kfile_host"
write_data(output_filename, flag=int(sys.argv[1]))
