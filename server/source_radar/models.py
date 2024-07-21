from source_radar.db import db


class Project(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    scans = db.relationship('Scan',
                            back_populates='project')


class Scan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    project_id = db.Column(db.Integer, db.ForeignKey('project.id'),
                           nullable=False)
    project = db.relationship('Project',
                              back_populates='scans')

    ready = db.Column(db.Boolean, default=False)