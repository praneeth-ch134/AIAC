def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines in '{file_path}': {len(lines)}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Example usage:
file_path = input("Enter the path to the .txt file: ")
count_lines_in_file(file_path)