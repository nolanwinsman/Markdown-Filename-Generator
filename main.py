import argparse
import os

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='A script to generate a Markdown file list.')

    # Add arguments
    parser.add_argument('directory', type=str, help='The directory to list files from')
    parser.add_argument('--output', '-o', type=str, default='file_list.md', help='Output filename (default: file_list.md)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose mode')
    parser.add_argument('--ignore-ext', nargs='+', default=[], help='List of file extensions to ignore (e.g., .git .tmp)')
    parser.add_argument('--ignore-dirs', nargs='+', default=['.git', '__pycache__'], help='List of directories to ignore')

    # Parse arguments
    args = parser.parse_args()

    return args

def generate_markdown_file_list(directory, output_file='file_list.md', verbose=False, ignore_ext=[], ignore_dirs=[]):
    """Generate a Markdown file list recursively from the specified directory."""
    print(f"Listing files from directory: {directory}")
    print(f"Output file will be: {output_file}")
    if verbose:
        print("Verbose mode enabled")
    print(f"Ignoring file extensions: {ignore_ext}")
    print(f"Ignoring directories: {ignore_dirs}")

    # Initialize list to hold all files
    all_files = []

    # Recursively traverse the directory tree
    for root, dirs, files in os.walk(directory):
        # Exclude ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for filename in sorted(files):  # Sort files alphabetically
            _, ext = os.path.splitext(filename)
            if ext.lower() in ignore_ext:
                continue  # Skip ignored file extensions
            
            filepath = os.path.join(root, filename)
            relative_path = os.path.relpath(filepath, directory)
            all_files.append((relative_path, ''))

        for dir_name in sorted(dirs):  # Sort directories alphabetically
            dir_path = os.path.join(root, dir_name)
            relative_path = os.path.relpath(dir_path, directory)
            all_files.append((f"{relative_path}{os.sep}", ''))  # Append directory path with trailing separator

    # Determine the maximum filename length
    max_filename_length = max(len(filename) for filename, _ in all_files)

    # Calculate the spacing based on the maximum filename length
    filename_description_spacing = max_filename_length + 5  # Adjust spacing as needed

    # Generate Markdown file list
    with open(output_file, 'w') as f:
        f.write(f"{'Filename':<{filename_description_spacing}}Description\n")
        f.write("-" * (filename_description_spacing + 15) + "\n")
        for filename, description in all_files:
            f.write(f"{filename:<{filename_description_spacing}}| {description}\n")
        f.write("-" * (filename_description_spacing + 15) + "\n")

def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Generate Markdown file list
    generate_markdown_file_list(args.directory, args.output, args.verbose, args.ignore_ext, args.ignore_dirs)

if __name__ == '__main__':
    main()
