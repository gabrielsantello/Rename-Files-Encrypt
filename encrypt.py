import os
import csv
import random

def rename_files():
    # Get the list of all files in the current directory
    files = os.listdir()

    # List of possible file extensions
    extensions = [
    '.3gp', '.7z', '.apk', '.avi', '.bin', '.cab', '.dat', '.db', '.dll',
    '.dmg', '.flv', '.h', '.jar', '.java', '.js', '.jsp', '.log', '.m4a',
    '.mov', '.mp3', '.mp4', '.mpeg', '.pkg', '.pl', '.rar', '.rpm', '.sql',
    '.tar.gz', '.vb', '.vbs', '.wav', '.wmv', '.zip', '.aiff', '.c', '.cpp'
]


    # Create a text file and write the names of all files into it along with their new names
    j = 0
    with open('file_list.txt', 'w') as f:
        for i, file in enumerate(files):
            # If the file is the text file we just created or a directory, skip it
            if file == 'file_list.txt' or file == 'decrypt.py' or not os.path.isfile(file):
                continue
            # Get the original extension of the file
            original_extension = os.path.splitext(file)[1]
            # Choose a random extension for the new file name that is not the same as the original extension
            new_extension = original_extension
            while new_extension == original_extension:
                new_extension = random.choice(extensions)
            new_name = str(j) + new_extension
            f.write(file + ',' + new_name + '\n')
            # Rename the file
            os.rename(file, new_name)
            j += 1

    # Finally, rename the text file as well
    last_number = str(j)
    os.rename('file_list.txt', last_number + '.dll')

if __name__ == "__main__":
    rename_files()