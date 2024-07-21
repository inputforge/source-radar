from flask import Flask
from flask_migrate import Migrate

from source_radar.api import api
from source_radar.db import db

app = Flask(__name__)
app.config.from_object('source_radar.config.Config')
db.init_app(app)
api.init_app(app)

migrate = Migrate(app, db)
