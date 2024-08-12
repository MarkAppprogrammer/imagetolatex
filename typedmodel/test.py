import os

def compare_folders(folder1, folder2):
    # Get the list of filenames in both folders
    files_folder1 = set(os.listdir(folder1))
    files_folder2 = set(os.listdir(folder2))

    # Normalize filenames to lower case to ensure case-insensitive comparison
    files_folder1 = set(f.lower() for f in files_folder1)
    files_folder2 = set(f.lower() for f in files_folder2)

    # Find missing files
    missing_in_folder2 = files_folder1 - files_folder2
    missing_in_folder1 = files_folder2 - files_folder1

    # Print results
    if missing_in_folder2:
        print(f"Files in '{folder1}' but not in '{folder2}':")
        for file in sorted(missing_in_folder2):
            print(file)
    else:
        print(f"All files in '{folder1}' are present in '{folder2}'.")

    if missing_in_folder1:
        print(f"\nFiles in '{folder2}' but not in '{folder1}':")
        for file in sorted(missing_in_folder1):
            print(file)
    else:
        print(f"All files in '{folder2}' are present in '{folder1}'.")

if __name__ == "__main__":
    folder1 = r'C:\Users\shado\OneDrive\Desktop\imagetolatex\data\formula_images'
    folder2 = r'C:\Users\shado\OneDrive\Desktop\imagetolatex\data\fixed_formula_images'
    compare_folders(folder1, folder2)
