import os
import zipfile

from pathspec import PathSpec
from pathspec.patterns.gitwildmatch import GitWildMatchPattern

# Create a zip of current directory excluding files in .gitignore recursively list all files in the directory
# and create a zip file

with open(".gitignore") as f:
    spec_text = f.read()
    # Create a PathSpec object from the .gitignore file
    spec = PathSpec.from_lines(GitWildMatchPattern, ['.git/', *spec_text.splitlines()])

def check_if_ignored(file: str):
    return spec.match_file(file)


def create_zip(directory: str, zip_name: str):
    with zipfile.ZipFile(zip_name, mode="w") as archive:
        for root, _, files in os.walk(directory):
            for file in files:
                path = os.path.join(root, file)
                # Get the relative path of the file from the directory
                relpath = os.path.relpath(path, directory)
                # Check if the file should be ignored
                if not check_if_ignored(relpath):
                    print(f"Adding {relpath} to zip")
                    archive.write(path, relpath)
