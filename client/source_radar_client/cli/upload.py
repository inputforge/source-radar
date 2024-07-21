import logging
import os
import tempfile
from collections import defaultdict

import click

from source_radar_client.analyzer import Analyzer
from source_radar_client.cli.bootstrap import bootstrap
from source_radar_client.client import upload_scan
from source_radar_client.create_zip import create_zip

log = logging.getLogger(__name__)


@click.command()
@click.option('--config-file', type=click.File('rb'), help='Path to the configuration file',
              default='source-radar.toml')
def upload(config_file: click.File):
    config, registry = bootstrap(config_file)

    analyzer = Analyzer(registry)

    messages = defaultdict(list)
    for _id, message in analyzer.analyze(config['linters'], config['roots']):
        messages[message.file].append({
            'line': message.location.start.line,
            'column': message.location.start.column,
            'message': message.content,
            'severity': message.severity.name.lower(),
            'code': message.code,
            'linter': _id
        })

    server = config['server']
    project = config['project']

    with tempfile.NamedTemporaryFile(suffix=".zip") as temp:
        create_zip(os.getcwd(), temp.name)
        log.info("Created zip file at %s", temp.name)
        upload_scan(server, project, temp.name, messages)
