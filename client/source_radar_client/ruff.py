# execute ruff command and read the output as json
import json
import subprocess
from pathlib import Path
from typing import ClassVar, Iterable

from source_radar_client.plugins.base import BasePlugin, Context
from source_radar_client.plugins.model import Severity, Message, Location, Position


class RuffLint(BasePlugin):
    id: ClassVar[str] = "ruff"

    def execute(self, context: Context) -> Iterable[Message]:
        command = ['ruff', 'check', '--output-format=json', '--exit-zero', str(context.base_dir)]
        output = subprocess.check_output(command)
        output_json = json.loads(output.decode('utf-8'))

        for issue in output_json:
            yield Message(
                code=issue['code'],
                location=Location(
                    start=Position(
                        line=issue['location']['row'],
                        column=issue['location']['column'],
                    ),
                    end=Position(
                        line=issue['end_location']['row'],
                        column=issue['end_location']['column'],
                    ),
                ),
                file=str(Path(issue['filename']).relative_to(context.base_dir)),
                severity=Severity.MINOR,
                content=issue['message'],
            )
