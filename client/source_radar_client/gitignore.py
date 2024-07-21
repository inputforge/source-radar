import os
from pathlib import Path

from pathspec import PathSpec
from pathspec.patterns.gitwildmatch import GitWildMatchPattern


class Matcher:
    def __init__(self, base_path: Path, spec: PathSpec | None):
        self.base_path = base_path
        self.spec = spec

    def match_file(self, file: Path) -> bool:
        if self.spec is None:
            return False

        return self.spec.match_file(os.path.relpath(file, self.base_path))


def load_gitignore(directory: Path) -> Matcher:
    try:
        with open(directory / ".gitignore") as f:
            spec_text = f.read()
            return Matcher(directory, PathSpec.from_lines(GitWildMatchPattern, spec_text.splitlines()))
    except FileNotFoundError:
        return Matcher(directory, None)
