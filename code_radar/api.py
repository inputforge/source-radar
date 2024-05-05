import os

from flask import request
from flask_restx import Resource, Api, fields
from db import db
from code_radar.model import Project, Scan


api = Api()

# request dto
project_model = api.model('Project', {
    'name': fields.String(required=True)
})

scan_model = api.model('Scan', {
    'name': fields.String(required=True)

})


# Resource for creating a Project
@api.route('/projects')
class ProjectCreation(Resource):
    @api.expect(project_model)
    def post(self):
        project = Project(name=api.payload['name'])
        db.session.add(project)
        db.session.commit()
        return {'message': 'Project created successfully'}, 201


# Resource for creating a Scan
@api.route('/projects/<int:project_id>/scans')
class ScanCreation(Resource):
    @api.expect(scan_model)
    def post(self, project_id):
        project = Project.query.get(project_id)
        if project:
            new_scan = Scan(project=project)
            db.session.add(new_scan)
            db.session.commit()
            return {'message': 'Scan created successfully'}, 201
        else:
            return {'error': 'Project not found'}, 404


# upload zip file

# request dto
file_upload_model = api.model('FileUpload', {
    'file': fields.String(required=True)
})


# api for uploading zip file
@api.route('/upload')
class FileUpload(Resource):
    @api.expect(file_upload_model)
    def post(self):
        if 'file' not in request.files:
            return {'error': 'No file part'}, 400
        file = request.files['file']
        file.save(os.path.join('/tmp', 'uploaded.zip'))
        return {'message': 'File uploaded successfully'}, 201
