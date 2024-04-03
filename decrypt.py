import csv
import os
import re

def revert_files():
    # Get the list of all files in the current directory
    files = os.listdir()

    # Find the file with the highest number in its name
    highest_number = -1
    file_with_highest_number = None
    for file in files:
        # Extract all numbers from the file name
        numbers = re.findall(r'\d+', file)
        if numbers:
            # Get the highest number in the file name
            highest_in_file = max(map(int, numbers))
            if highest_in_file > highest_number:
                highest_number = highest_in_file
                file_with_highest_number = file

    # Rename the file with the highest number to 'file_list.txt'
    if file_with_highest_number is not None:
        os.rename(file_with_highest_number, 'file_list.txt')

    # Open the file list
    with open('file_list.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            original_name, new_name = row[0], row[1]
            # Check if the file with the new name exists
            if os.path.isfile(new_name):
                # Rename the file back to its original name
                os.rename(new_name, original_name)

    # Delete the 'file_list.txt' file
    if os.path.exists('file_list.txt'):
        os.remove('file_list.txt')

if __name__ == "__main__":
    revert_files()