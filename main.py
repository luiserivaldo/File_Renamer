# Python 3 code to rename multiple files in a directory or folder

# importing os module
import os


# Function to rename multiple files
def main():
    print("This is a file renamer tool. \n")
    directory = input(str("Enter the folder name/path where files need to be renamed: "))
    if directory == "":
        print("Directory set to 'images', \n")  # speeds up the code testing by specifying the folder as prepared
        directory = "images"
    old_word = input(str("Enter the word that needs to be replaced: "))
    new_word = input(str("Enter the new word to replace the original: "))

    file_renamer(directory, old_word, new_word)
    print("Completed!")


def file_renamer(directory, old_word, new_word):
    count = 0
    for file in os.listdir(directory):
        if old_word in file:
            os.rename(os.path.join(file),
                      os.path.join(file.replace(old_word, new_word)))
        count = count + 1
    print(count, " files have been renamed.")


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
