# execute ruff command and read the output as json
import subprocess


def execute():
    command = ['ruff', 'check', '--output-format=json','--exit-zero']
    output = subprocess.check_output(command)
    return output.decode('utf-8')
