import importlib
import tomllib
from typing import Tuple, Any

import click

from source_radar_client.plugins.registry import PluginRegistry


def bootstrap(config_file: click.File) -> Tuple[dict[str, Any], PluginRegistry]:
    with config_file as f:
        config = tomllib.load(f)
        registry = PluginRegistry()

        for plugin in config.get('plugins', []):
            module_name, class_name = plugin.rsplit('.', 1)
            module = importlib.import_module(module_name)
            registry.register(getattr(module, class_name))

        return config, registry
