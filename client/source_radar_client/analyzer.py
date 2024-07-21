import logging
from collections.abc import Generator
from pathlib import Path
from typing import Sequence, Tuple

from source_radar_client.plugins.base import Context
from source_radar_client.plugins.model import Message
from source_radar_client.plugins.registry import PluginRegistry

log = logging.getLogger(__name__)


class Analyzer:
    def __init__(self, registry: PluginRegistry):
        self.registry = registry

    def analyze(self, linters: Sequence[str], roots: Sequence[str]) -> Generator[Tuple[str, Message], None, None]:
        for root in roots:
            context = Context(base_dir=(Path(root).absolute()))

            for linter in linters:
                log.info("Running linter %s", linter)
                linter_class = self.registry.get_plugin(linter)
                linter_instance = linter_class()
                yield from ((linter_class.id, m) for m in linter_instance.execute(context))
