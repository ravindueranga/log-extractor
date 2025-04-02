import os
import shutil
import zipfile

TARGET_LOG_FILE = "stzlog.log"

def get_top_most_folder(path):
    while True:
        parent = os.path.dirname(path)
        if parent == path:  # If the parent is the same as the current path, we've reached the root
            break
        path = parent
    return os.path.basename(path)

def find_and_copy_stz_logs(root_dir, destination_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.zip'):
                zip_path = os.path.join(dirpath, filename)
                zip_name = os.path.splitext(filename)[0]  # Get the zip file name without the extension
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    print(f"Processing zip file: {zip_path}")
                    for zip_info in zip_ref.infolist():
                        # Check if the file ends with 'stzlog.log' regardless of its path inside the zip
                        if zip_info.filename.endswith(TARGET_LOG_FILE):
                            # Extract the file to the destination directory
                            source_file = zip_ref.extract(zip_info, destination_dir)
                            # Use the zip file's name in the destination file name
                            destination_file = os.path.join(destination_dir, f"{zip_name}_stz.log")
                            shutil.copy2(source_file, destination_file)
                            print(f"Copied {source_file} to {destination_file}")

if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
    destination_directory = os.getcwd()  # Directory where the script is run
    find_and_copy_stz_logs(root_directory, destination_directory)
