File Organizer

A simple Python automation tool that organizes files into folders based on their file extensions.

Overview

File Organizer helps reduce the time spent manually sorting files.

The program scans a selected folder, identifies supported file types, creates the appropriate category folders, and moves the files into them automatically.

Features

- Organizes images, documents, music, and videos
- Supports multiple file extensions
- Automatically creates category folders
- Handles uppercase and lowercase extensions
- Skips unsupported file types
- Prevents duplicate files from being overwritten
- Validates the folder path
- Displays a summary after organization

Supported File Types

Category| Extensions
Images| ".jpg", ".jpeg", ".png", ".gif"
Documents| ".pdf", ".doc", ".docx", ".txt", ".csv"
Music| ".mp3", ".wav"
Videos| ".mp4", ".mkv"

Example

Before:

Downloads/
├── photo.jpg
├── report.pdf
├── song.mp3
└── video.mp4

After:

Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Music/
│   └── song.mp3
└── Videos/
    └── video.mp4

Requirements

- Python 3
- No external Python packages required

How to Run

Run the program:

python file_organizer.py

Enter the path of the folder you want to organize when prompted.

Safety

The program moves files rather than deleting them. However, users should test the tool on a non-critical folder before using it on important files.

Project Purpose

This project demonstrates practical Python skills including:

- File-system automation
- Working with directories and file paths
- File extension handling
- Conditional logic
- Dictionaries
- Error handling
- Python standard-library modules
- Git and GitHub project management

Author

Ahmad

Built as a practical Python automation project and portfolio demonstration.
