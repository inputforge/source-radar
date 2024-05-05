import io

import requests


def upload_scan(config, temp_zip_file: str, scan_json: str):
    project_id = config.get("project_id")
    server = config.get("server")

    response = requests.post(f"{server}/projects/{project_id}/scans", json={"name": "scan1"})
    response.raise_for_status()
    scan = response.json()
    stream_str = io.BytesIO(scan_json.encode())

    with open(temp_zip_file, "rb") as f:
        response = requests.post(f"{server}/projects/{project_id}/scans/{scan['id']}/upload",
                                 files={"code": f, "scan_result": stream_str})
        response.raise_for_status()
