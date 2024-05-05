import os

from code_radar_client.create_zip import create_zip

if __name__ == "__main__":
    create_zip(os.getcwd(), "/tmp/zipfile.zip")