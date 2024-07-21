from dataclasses import dataclass
from enum import StrEnum
from dataclasses_json import DataClassJsonMixin


class Severity(StrEnum):
    MINOR = "MINOR"
    MAJOR = "MAJOR"
    CRITICAL = "CRITICAL"
    BLOCKER = "BLOCKER"


@dataclass
class Position(DataClassJsonMixin):
    line: int
    column: int


@dataclass
class Location(DataClassJsonMixin):
    start: Position
    end: Position


@dataclass
class Message(DataClassJsonMixin):
    code: str
    file: str
    location: Location
    content: str
    severity: Severity
