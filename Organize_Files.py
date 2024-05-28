import os
import shutil
import hashlib

def get_platform_separator():
    """Returns the platform-specific path separator."""
    return os.sep

def calculate_file_hash(file_path, hash_algorithm='md5'):
    """
    Calculates the hash of a file using the specified hash algorithm.
    Args:
        file_path: The path to the file.
        hash_algorithm: The hash algorithm to use (default is 'md5').
    Returns:
        The calculated hash of the file.
    """
    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def organize_files(directory):
    """
    Organizes files in a directory by moving them into folders based on their types
    and identifies duplicate files.
    Args:
        directory: The directory path to organize.
    """
    separator = get_platform_separator()
    current_dir = os.path.dirname(os.path.realpath(__file__))

    try:
        # Check if user provided a directory path
        if directory:
            os.chdir(directory)
        else:
            os.chdir(current_dir)

        # Create dictionaries to store extension counts, folder paths, and file hashes
        extension_counts = {}
        folder_paths = {}
        file_hashes = {}
        duplicates_folder = os.path.join('.', 'Duplicates')

        # Create the Duplicates folder if it doesn't exist
        if not os.path.exists(duplicates_folder):
            os.makedirs(duplicates_folder)

        # Loop through all files in the directory (not recursively)
        for file in os.listdir('.'):
            if os.path.isfile(file):
                # Get the file extension (lowercase)
                extension = os.path.splitext(file)[1].lower()

                # Calculate file hash
                file_path = os.path.join('.', file)
                file_hash = calculate_file_hash(file_path)

                # Check for duplicates
                if file_hash in file_hashes:
                    duplicate_folder = os.path.join(duplicates_folder, extension.lstrip('.'))
                    if not os.path.exists(duplicate_folder):
                        os.makedirs(duplicate_folder)
                    shutil.move(file_path, os.path.join(duplicate_folder, file))
                    print(f"Duplicate found and moved: {file_path} to {duplicate_folder}")
                    continue
                else:
                    file_hashes[file_hash] = file_path

                # Update extension count
                if extension in extension_counts:
                    extension_counts[extension] += 1
                else:
                    extension_counts[extension] = 1

                # Determine destination folder based on file extension
                if extension and extension != '.':  # Skip files with no extension
                    folder_path = os.path.join('.', extension.lstrip('.'))
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    folder_paths[extension] = folder_path

                    # Move the file to its corresponding folder
                    destination_file = os.path.join(folder_path, file)
                    shutil.move(file_path, destination_file)

        # Print summary of organized files
        print(f"File organization completed in directory: {os.getcwd()}")
        for extension, count in extension_counts.items():
            folder = extension.lstrip('.')
            print(f"\t- {count} {extension} file(s) moved to {folder} folder.")

    except (OSError, PermissionError) as e:
        print(f"Error organizing files: {e}")

    finally:
        # Always change back to the original working directory
        os.chdir(current_dir)

# No user input for directory (use script's location)
directory = ""

# Organize files
organize_files(directory)
