File Organizer

A simple Python automation tool that organizes files into folders based on their file extensions.

Overview

File Organizer helps reduce the time spent manually sorting files.

The program scans a selected folder, identifies supported file types, automatically creates category folders, and moves the files into the appropriate folders.

Features

- Organizes images, documents, music, and videos
- Supports multiple file extensions
- Automatically creates category folders
- Handles uppercase and lowercase extensions
- Skips unsupported file types
- Prevents existing files from being overwritten
- Validates the folder path
- Displays an organization summary
- Uses only Python's standard library

Supported File Types

Category| Extensions
Images| ".jpg", ".jpeg", ".png", ".gif"
Documents| ".pdf", ".doc", ".docx", ".txt", ".csv"
Music| ".mp3", ".wav"
Videos| ".mp4", ".mkv"

Example

Before

Downloads/
├── photo.jpg
├── report.pdf
├── song.mp3
└── video.mp4

After

Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Music/
│   └── song.mp3
└── Videos/
    └── video.mp4

How It Works

1. The user provides the path to a folder.
2. The program checks that the folder exists.
3. Files are scanned one by one.
4. The file extension determines its category.
5. The required category folder is created automatically.
6. The file is moved into that category folder.
7. Unsupported files are left untouched.
8. Existing files are not overwritten.
9. A summary is displayed when the process finishes.

Requirements

- Python 3
- No external Python packages required

How to Run

Run:

python file_organizer.py

The program will ask:

Enter folder path:

Enter the path of the folder you want to organize.

Safety

The program moves files rather than deleting them.

However, it is recommended to test the program on a non-critical folder before using it with important files.

Technologies

- Python
- "os"
- "shutil"
- Git
- GitHub

Skills Demonstrated

This project demonstrates practical skills in:

- Python programming
- File-system automation
- Directory and file management
- File extension handling
- Dictionaries
- Conditional logic
- Error handling
- Python standard-library modules
- Git version control
- GitHub project management

Project Structure

file-organizer/
├── file_organizer.py
├── README.md
└── .gitignore

Future Improvements

Possible future versions could include:

- More supported file types
- Custom categories
- A graphical user interface
- A preview mode before moving files
- Logging
- Configurable organization rules

Author

Ahmad

Built as a practical Python automation project and portfolio demonstration.
