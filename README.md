# File Organizer

File Organizer is a Python script that organizes files in a directory by moving them into folders based on their types (file extensions), while efficiently identifying and handling duplicate files.

## Features

- **File Organization**: Files are categorized into folders corresponding to their extensions for better organization.
- **Duplicate Detection**: The script calculates file hashes to detect duplicate files and moves them to a designated "Duplicates" folder.
- **Efficient Handling**: Utilizes platform-specific functions for file operations and efficient hash calculation for improved performance.

## Usage

1. Clone the repository or download the Python script (`file_organizer.py`) to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script by executing the command: `python file_organizer.py`.
4. Optionally, provide a directory path as an argument to organize files in a specific directory: `python file_organizer.py /path/to/directory`.

## Requirements

- Python 3
- `os`, `shutil`, `hashlib` standard libraries

## License

This project is Open to anyone who wants to use this.
