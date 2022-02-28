# Python 3 code to rename multiple files in a directory or folder

# importing os module
import os

# Function to rename multiple files
import sys


def main():
    print("This is a file renamer tool. \n")
    directory = input(str("Enter the folder name/path where files need to be renamed: "))
    if directory == "":
        print("No custom path. Directory set to 'images'. \n")
        directory = "images/"
        # set target directory to "images" folder within project folder
    else:
        directory += '/'
    old_word = input(str("Enter the word that needs to be replaced: "))
    new_word = input(str("Enter the new word to replace the original: "))

    try:
        file_renamer(directory, old_word, new_word)
        # revert_name(directory, new_word, old_word)
        repeat_tool()
    except FileNotFoundError:
        print("No file or path detected. Current directory is ", directory, ".")


def file_renamer(directory, old_word, new_word):
    count = 0
    for file in os.listdir(directory):
        if old_word in file:
            os.rename(os.path.join(directory + file),
                      os.path.join(directory + file.replace(old_word, new_word)))
            count = count + 1  # counts how many times function has been executed
    print(count, "files have been renamed. \n")
    print("Please check your files if they have been properly renamed. \n")


def revert_name(directory, new_word, old_word):
    revert_changes = input(str("Would you like to revert the changes? [Y/N] "))
    if revert_changes.lower() == "y":
        count = 0
        for file in os.listdir(directory):
            if new_word in file:
                os.rename(os.path.join(directory + file),
                          os.path.join(directory + file.replace(new_word, old_word)))
                # inverse process of renaming, results in the original file names
                count = count + 1
        print(count, "files have been reverted. \n")
    else:
        print("No files reverted.")


def repeat_tool():
    repeat_input = input(str("Would you like to rename more files? [Y/N] "))
    if repeat_input.lower() == "y":
        print("Restarting tool... \n")
        main()
    # elif repeat_input.lower == "n":
        # print(repeat_input)
        # print("Thank you for using the tool!")
    else:
        print("Thank you for using the tool!")
        return


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
