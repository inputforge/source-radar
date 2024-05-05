# execute ruff command and read the output as json
import subprocess

from code_radar_client.config import Config


def execute(config: Config):
    src = config.get("sources.directories", [])

    command = ['ruff', '--output-format=json', '--exit-zero', 'check', *src]
    output = subprocess.check_output(command)
    return output.decode('utf-8')
