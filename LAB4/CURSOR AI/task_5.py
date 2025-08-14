def count_lines_in_file():
    file_path = input("Enter the path to the .txt file: ").strip()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(f"Number of lines in the file: {num_lines}")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
count_lines_in_file()