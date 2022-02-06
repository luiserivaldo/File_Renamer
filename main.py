# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os


# Function to rename multiple files
def main():
    folder = input(str("Enter the file directory: "))
    find_target = input(str("Enter the word that needs to be replaced: "))
    replace_target = input(str("Enter the desired word to replace the original: "))

    file_renamer(folder, find_target, replace_target)


def file_renamer(folder, find_target, replace_target):
    for file in os.listdir():
        if find_target(main) in file:
            os.rename(os.path.join(folder, file),
                      os.path.join(folder, file.replace(find_target, replace_target)))


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
