import logging

from source_radar_client.cli.group import cli

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    cli()
