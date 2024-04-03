# File Renaming Scripts

This repository contains two Python scripts: `encrypt.py` and `decrypt.py`.

## encrypt.py

This script renames all the files in the current directory to a number followed by a random extension from a predefined list. The original and new names of the files are stored in a text file. The text file is then renamed to a number followed by '.dll'.

### Usage

1. Place the `encrypt.py` script in the directory containing the files you want to rename.
2. Run the script using the command `python encrypt.py`.
3. All the files in the directory, except for 'encrypt.py' and 'decrypt.py', will be renamed. The original and new names of the files will be stored in a text file, which will also be renamed.

## decrypt.py

This script reverts the changes made by `encrypt.py`. It renames the files back to their original names based on the information in the text file created by `encrypt.py`.

### Usage

1. After running `encrypt.py`, place the `decrypt.py` script in the same directory.
2. Run the script using the command `python decrypt.py`.
3. The files will be renamed back to their original names, and the text file will be deleted.

Please note that these scripts should be used with caution. Make sure to back up your files before running these scripts, as the changes they make are irreversible.