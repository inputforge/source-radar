import logging
import os
import tempfile
import zipfile

from code_radar_client.create_zip import create_zip

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    with tempfile.NamedTemporaryFile(suffix=".zip") as temp:
        create_zip(os.getcwd(), temp.name)
        log.info(f"Created zip file at {temp.name}")
