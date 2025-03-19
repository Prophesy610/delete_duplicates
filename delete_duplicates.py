import os
import hashlib

def calculate_file_hash(file_path):
    """
    Calculate the SHA256 hash of a file.
    """
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_and_delete_duplicates(folder_path):
    """
    Scan the folder and its subfolders for duplicate files and delete them.
    """
    file_hashes = {}
    duplicate_count = 0

    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_file_hash(file_path)

            if file_hash in file_hashes:
                print(f"Duplicate found: {file_path} (duplicate of {file_hashes[file_hash]})")
                os.remove(file_path)
                duplicate_count += 1
            else:
                file_hashes[file_hash] = file_path

    print(f"Scanning complete. {duplicate_count} duplicate(s) deleted.")

def correct_folder_path(folder_path):
    """
    Attempt to correct the folder path if invalid by applying solution 1 (raw string handling).
    """
    # Ensure the path is treated as a raw string and normalized
    folder_path = folder_path.replace('\\', '/')
    folder_path = os.path.expanduser(folder_path.strip())
    return os.path.abspath(folder_path)

if __name__ == "__main__":
    print("Drag and drop the folder into this terminal window, then press Enter.")
    folder_to_scan = input("Enter the folder path to scan for duplicates: ").strip()
    folder_to_scan = correct_folder_path(folder_to_scan)

    if os.path.isdir(folder_to_scan):
        find_and_delete_duplicates(folder_to_scan)
    else:
        print("Invalid folder path. Please try again.")
