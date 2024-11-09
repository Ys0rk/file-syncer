#!/usr/bin/python3

import os
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def read_file(file_path):
    """Reads the contents of a file and returns a list of lines."""
    if not os.path.exists(file_path):
        print(Fore.RED + f"File '{file_path}' does not exist!")
        return []
    
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def write_to_file(file_path, lines):
    """Appends new lines to a file."""
    with open(file_path, 'a') as f:
        for line in lines:
            f.write(line + '\n')

def overwrite_file(file_path, lines):
    """Overwrites a file with the provided lines."""
    with open(file_path, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def compare_and_move_content(oldfile_path, newfile_path):
    """Compares content of newfile.txt and oldfile.txt, moves new content to oldfile if not present."""
    # Read content from both files
    old_content = set(read_file(oldfile_path))
    new_content = read_file(newfile_path)

    # List for new content that needs to be moved
    to_move = []

    # Check which lines from newfile need to be moved
    for line in new_content:
        if line not in old_content:
            to_move.append(line)

    # If there's new content to move, prepend it to oldfile and clear newfile
    if to_move:
        # Prepend new content to old file (i.e., move the new content to the front)
        current_old_content = read_file(oldfile_path)
        combined_content = to_move + current_old_content  # New content first

        # Overwrite the oldfile with the combined content
        overwrite_file(oldfile_path, combined_content)

        # Print the moved content in green
        print(Fore.GREEN + f"\nMoved {len(to_move)} new item(s) to {oldfile_path}:")
        for line in to_move:
            print(Fore.GREEN + line)

        # Clear the content of the newfile after moving the content
        open(newfile_path, 'w').close()
        print(Fore.YELLOW + f"\nCleared content in {newfile_path}")

    else:
        print(Fore.RED + "\nNo new content to move.")

    # Print the content that already exists in oldfile in red
    already_in_oldfile = [line for line in new_content if line in old_content]
    if already_in_oldfile:
        print(Fore.RED + f"\nThe following content already exists in {oldfile_path}:")
        for line in already_in_oldfile:
            print(Fore.RED + line)

def main():
    # Prompt user for file paths
    oldfile_path = input("Enter the path of the old file (oldfile.txt): ")
    newfile_path = input("Enter the path of the new file (newfile.txt): ")

    # Compare and move content
    compare_and_move_content(oldfile_path, newfile_path)

if __name__ == "__main__":
    main()

