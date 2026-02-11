import os

# Function to process each text file and convert it to .inp format
def convert_to_inp(filename):
    # Read the data from the text file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove the first line (header)
    lines = lines[1:]

    # Extract the base name from the filename (without the extension)
    base_name = os.path.splitext(filename)[0]

    # Prepare the header for the .inp file with the unique name
    inp_content = f"*Amplitude, name=\"{base_name}\"\n"

    # Prepare a list to store formatted values
    formatted_values = []

    # Process each line from the input text file
    for line in lines:
        # Split the line into time and amplitude
        time, amplitude = line.strip().split(',')
        # Convert to float and format with commas and dots
        time = float(time)
        amplitude = float(amplitude)
        # Append the formatted pair to the list
        formatted_values.append(f"{time:.6f}, {amplitude:.6f}")

    # Now group the formatted values into rows of 8 pairs per line
    row_size = 8  # 8 values (4 time-amplitude pairs) per line
    rows = [", ".join(formatted_values[i:i + row_size]) for i in range(0, len(formatted_values), row_size)]

    # Add the rows to the inp_content
    for row in rows:
        inp_content += "    " + row + "\n"  # Indent each line

    # Write to a new .inp file
    inp_filename = filename.replace(".txt", ".inp")
    with open(inp_filename, 'w') as inp_file:
        inp_file.write(inp_content)

    print(f"Converted {filename} to {inp_filename}")

# Function to convert all .txt files in the current directory
def convert_all_files():
    # Get all text files in the current directory
    for filename in os.listdir():
        if filename.endswith(".txt"):
            convert_to_inp(filename)

# Run the conversion
convert_all_files()
