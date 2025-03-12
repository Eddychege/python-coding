def process_file():
    # Ask user for input file name
    input_filename = input("Enter the name of the file you want to read: ")

    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as input_file:
            # Read the contents of the file
            content = input_file.read()

            # Print the contents of the file
            print(content)
            print(f"Successfully read file: {input_filename}")

            # Create output filename based on input filename
            if '.' in input_filename:
                base_name = input_filename.rsplit('.', 1)[0]
                extension = input_filename.rsplit('.', 1)[1]
                output_filename = f"{input_filename}_modified.{extension}"
            else:
                output_filename = f"{input_filename}_modified"

            # Ask user if they want to use default filename or specify a new one
            print(f"Default output filename: {output_filename}")
            custom_filename = input("Press Enter to use default or type a new filename: ")
            if custom_filename:
                output_filename = custom_filename

            # Modify the content (convert to uppercase and add a line numbers)
            modified_lines = []
            for i, line in enumerate(content.split('\n'), 1):
                modified_lines.append(f"{i}: {line.upper()}")
            modified_content = '\n'.join(modified_lines)

            # Write modified content to output file
            try:
                with open(output_filename, 'w') as output_file:
                    output_file.write(modified_content)
                    print(f"Successfully wrote modified content to file: {output_filename}")
            except IOError as e:
                print(f"Error writing to output file: {e}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to access the file '{input_filename}'.")
    except IOError as e:
        print(f"Error reading the file: {e}")
    except UnicodeDecodeError:
        print(f"Error: The file '{input_filename}' contains characters that could not be decoded.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the process_file function
if __name__ == "__main__":
    print("File Processing Program")
    print("-----------------------")
    process_file()

    # Ask if user wants to process another file:
    while input("\nProcess another file? (y/n): ").lower().startswith('y'):
        process_file()

    print("Program terminated. Adios!")


