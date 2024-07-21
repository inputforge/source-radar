import click

from source_radar_client.cli.analyze import analyze
from source_radar_client.cli.upload import upload


@click.group('source-radar')
def cli():
    pass


cli.add_command(analyze)
cli.add_command(upload)
