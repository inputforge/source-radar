from flask import Flask
from flask_migrate import Migrate

from code_radar.api import api
from code_radar.db import db

app = Flask(__name__)
app.config.from_object('code_radar.config.Config')
db.init_app(app)
api.init_app(app)

migrate = Migrate(app, db)
