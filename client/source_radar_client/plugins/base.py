from abc import ABC
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

from source_radar_client.plugins.model import Message


@dataclass
class Context:
    base_dir: Path


class BasePlugin(ABC):
    id: ClassVar[str]

    def __new__(cls, *args, **kwargs):
        if getattr(cls, "id", "") == "":
            cls.id = cls.__name__

        return super().__new__(cls)

    def execute(self, context: Context) -> Iterable[Message]:
        raise NotImplementedError
