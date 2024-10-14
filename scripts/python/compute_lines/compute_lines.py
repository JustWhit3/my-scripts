import os
import argparse

def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return sum(1 for _ in file)

def count_lines_in_directory(directory, extensions):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                lines_in_file = count_lines_in_file(file_path)
                print(f'{file_path}: {lines_in_file} lines')
                total_lines += lines_in_file
    return total_lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count lines of code in multiple directories.")
    
    # Argument to take directories as input
    parser.add_argument('directories', nargs='+', help="List of directories to scan")
    
    # Argument to take file extensions as input
    parser.add_argument('-e', '--extensions', nargs='+', default=['.cpp', '.hpp', '.py', '.sh'], 
                        help="File extensions to include (e.g. -e .cpp .hpp)")
    
    args = parser.parse_args()

    total_lines = 0
    for dir in args.directories:
        print(f'\nScanning directory: {dir}')
        total_lines += count_lines_in_directory(dir, tuple(args.extensions))  # Convert list to tuple for endswith()

    print(f'\nTotal lines of code: {total_lines}')
