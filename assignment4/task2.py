# task2_write_append_file.py

def write_and_append_file(filename):
    # Write data to the file
    data = input("Enter initial text to write into the file: ")
    with open(filename, 'w') as file:
        file.write(data + '\n')

    # Append additional data
    extra_data = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(extra_data + '\n')

    # Read and display final content
    print("\nFinal content of the file:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# Sample usage
write_and_append_file("output.txt")
