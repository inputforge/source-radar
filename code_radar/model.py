from code_radar.db import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    scans = db.relationship('Scan',
                            back_populates='project')


class Scan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    project_id = db.Column(db.Integer, db.ForeignKey('project.id'),
                           nullable=False)
    project = db.relationship('Project',
                              back_populates='scans')
