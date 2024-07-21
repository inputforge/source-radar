import os
import zipfile
from pathlib import Path

from source_radar_client.gitignore import Matcher, load_gitignore

vcs_dirs = {".git"}


def _zip_dir(root: Path, directory: Path, archive: zipfile.ZipFile, matchers: list[Matcher]):
    """
    Recursively zip a directory, excluding files that match any of the patterns in the matchers list.
    :param root: Root directory of the zip
    :param directory: Current directory to zip
    :param archive: Handle to the zip file
    :param matchers: List of matchers to exclude files
    :return: None
    """
    matcher = load_gitignore(directory)
    matchers = matchers + [matcher]

    for f in os.listdir(directory):
        entry = directory / f
        if os.path.isdir(entry):
            if entry.name in vcs_dirs:
                continue
            if any(matcher.match_file(entry) for matcher in matchers):
                continue

            _zip_dir(root, entry, archive, matchers)
        else:
            if not any(matcher.match_file(entry) for matcher in matchers):
                archive.write(entry, entry.relative_to(root))


def create_zip(directory: str, zip_name: str):
    with zipfile.ZipFile(zip_name, mode="w") as archive:
        _zip_dir(Path(directory), Path(directory), archive, [])
