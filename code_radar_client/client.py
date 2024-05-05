import io

import requests


def upload_scan(temp_zip_file: str, scan_json: str):
    response = requests.post("http://127.0.0.1:5000/projects/1/scans", json={"name": "scan1"})
    response.raise_for_status()
    scan = response.json()
    stream_str = io.BytesIO(scan_json.encode())

    with open(temp_zip_file, "rb") as f:
        response = requests.post(f"http://127.0.0.1:5000/projects/1/scans/{scan['id']}/upload",
                                 files={"code": f, "scan_result": stream_str})
        response.raise_for_status()
