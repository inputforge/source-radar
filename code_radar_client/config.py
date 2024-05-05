import tomllib
from configparser import ConfigParser
from typing import Any, TypeVar

T = TypeVar("T")


class Config:
    def __init__(self, raw_config: dict[str, Any]):
        self.raw_config = raw_config

    def get(self, key: str, default: T = None) -> T:
        path = key.split(".")
        current = self.raw_config
        for p in path:
            if p not in current:
                return default
            current = current[p]

        return current


def load_config(config_file_path: str) -> Config:
    """
    Load a configuration INI file from the given path.
    :param config_file_path:
    :return:
    """
    with open(config_file_path, 'rb') as f:
        raw_config = tomllib.load(f)
        return Config(raw_config)
