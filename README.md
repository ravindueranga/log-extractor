# STZ Log Extractor

This Python script is designed to search for `.zip` files in a specified directory, extract a specific log file (`stzlog.log`) from them, and copy the extracted log file to a destination directory. The extracted log files are renamed using the name of the `.zip` file they were extracted from.

## Features

- Recursively searches for `.zip` files in the specified root directory.
- Extracts a specific log file (`stzlog.log`) from the `.zip` files.
- Renames the extracted log file using the name of the `.zip` file.
- Copies the renamed log file to the specified destination directory.

## Requirements

- Python 3.6 or higher
- The following Python modules:
  - `os`
  - `shutil`
  - `zipfile`

## Usage

### Output

For each `.zip` file processed, the script will:

1. Extract the `stzlog.log` file (if it exists).
2. Rename the extracted log file to `<zip_file_name>_stz.log`.
3. Copy the renamed log file to the destination directory.

### Example Output

If the script processes a `.zip` file named `example.zip` containing `stzlog.log`, the output will be:

```
Processing zip file: /path/to/root/example.zip
Copied /path/to/destination/stzlog.log to /path/to/destination/example_stz.log
```

## Configuration

The target log file name (`stzlog.log`) is defined as a constant in the script:

```python
TARGET_LOG_FILE = "stzlog.log"
```

You can modify this value if the target log file name changes.
