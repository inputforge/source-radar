import io
from typing import Any

import requests


def upload_scan(server: str, project: str, temp_zip_file: str, scan_json: Any):
    base_url = f"{server}/projects/{project}"
    response = requests.post(base_url + "/scans/", json={"name": "scan1"})
    response.raise_for_status()
    scan = response.json()
    stream_str = io.BytesIO(scan_json.encode())

    with open(temp_zip_file, "rb") as f:
        response = requests.post(f"{base_url}/scans/{scan['id']}/files",
                                 files={"code": f, "scan_result": stream_str})
        response.raise_for_status()
