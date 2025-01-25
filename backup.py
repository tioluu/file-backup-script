import os
import shutil

# Source and destination directories
source_dir = "source_folder"
backup_dir = "backup_folder"

# Create the backup directory if it doesn't exist
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Copy files from source to backup
for filename in os.listdir(source_dir):
    source_file = os.path.join(source_dir, filename)
    backup_file = os.path.join(backup_dir, filename)
    shutil.copy2(source_file, backup_file)

print(f"Files from '{source_dir}' have been backed up to '{backup_dir}'.")
