import os

from source_radar.app import app

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('scans', exist_ok=True)
    app.run(debug=True)
