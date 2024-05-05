import os
import tempfile

from code_radar_client.create_zip import create_zip

if __name__ == "__main__":
    with tempfile.NamedTemporaryFile() as temp:
        create_zip(os.getcwd(), temp.name)

