import logging
import os
import tempfile

from code_radar_client.client import upload_scan
from code_radar_client.create_zip import create_zip
from code_radar_client.ruff import execute

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    with tempfile.NamedTemporaryFile(suffix=".zip") as temp:
        create_zip(os.getcwd(), temp.name)
        log.info(f"Created zip file at {temp.name}")
        scan_json = execute()
        upload_scan(temp.name, scan_json)
