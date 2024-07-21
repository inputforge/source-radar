import click

from source_radar_client.analyzer import Analyzer
from source_radar_client.cli.bootstrap import bootstrap


@click.command()
@click.option('--config-file', type=click.File('rb'), help='Path to the configuration file', default='source-radar.toml')
def analyze(config_file: click.File):
    config, registry = bootstrap(config_file)

    analyzer = Analyzer(registry)

    for _id, message in analyzer.analyze(config['linters'], config['roots']):
        click.echo(
            f"{message.file}:{message.location.start.line}:{message.location.start.column}:[{_id}-{message.code}] {message.severity.name.lower()}: {message.content}"
        )
