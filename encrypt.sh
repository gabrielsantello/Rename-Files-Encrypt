#!/bin/bash

# List of possible file extensions
extensions=('.3gp' '.7z' '.apk' '.avi' '.bin' '.cab' '.dat' '.db' '.dll' '.dmg' '.flv' '.h' '.jar' '.java' '.js' '.jsp' '.log' '.m4a' '.mov' '.mp3' '.mp4' '.mpeg' '.pkg' '.pl' '.rar' '.rpm' '.sql' '.tar.gz' '.vb' '.vbs' '.wav' '.wmv' '.zip' '.aiff' '.c' '.cpp')

# Create a text file and write the names of all files into it along with their new names
j=0
for file in *; do
    # If the file is the text file we just created or a directory, skip it
    if [[ $file == 'file_list.txt' ]] || [[ $file == 'decrypt.py' ]] || [[ ! -f $file ]]; then
        continue
    fi
    # Get the original extension of the file
    original_extension="${file##*.}"
    # Choose a random extension for the new file name that is not the same as the original extension
    new_extension=$original_extension
    while [[ $new_extension == $original_extension ]]; do
        new_extension=${extensions[$RANDOM % ${#extensions[@]}]}
    done
    new_name="$j$new_extension"
    echo "$file,$new_name" >> file_list.txt
    # Rename the file
    mv -- "$file" "$new_name"
    ((j++))
done

# Finally, rename the text file as well
mv -- 'file_list.txt' "$j.dll"