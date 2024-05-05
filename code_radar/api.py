import os
import zipfile

from flask_restx import Resource, Api, fields
from werkzeug.datastructures import FileStorage

from code_radar.db import db
from code_radar.models import Project, Scan

api = Api(prefix='/api/v1', version='1.0', title='Code Radar API', doc="/api/v1/")

scan_model = api.model('Scan', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True)
})

# request dto
project_model = api.model('Project', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True),
})


# Resource for creating a Project
@api.route('/projects')
class ProjectResource(Resource):
    @api.expect(project_model)
    @api.marshal_with(project_model)
    def post(self):
        project = Project(name=api.payload['name'])
        db.session.add(project)
        db.session.commit()
        return {project}, 201

    @api.marshal_with(project_model)
    def get(self):
        return Project.query.all()


# Resource for creating a Scan
@api.route('/projects/<int:project_id>/scans')
class ScanCreation(Resource):
    @api.marshal_with(scan_model)
    @api.expect(scan_model)
    def post(self, project_id):
        project = Project.query.get_or_404(project_id)
        new_scan = Scan(project=project, name=api.payload['name'])
        db.session.add(new_scan)
        db.session.commit()
        return new_scan, 201

    @api.marshal_with(scan_model)
    def get(self, project_id):
        project = Project.query.get_or_404(project_id)
        return Scan.query.filter_by(project=project).all()


# upload zip file

# request dto
upload_parser = api.parser()
upload_parser.add_argument('code', location='files',
                           type=FileStorage, required=True)
upload_parser.add_argument('scan_result', location='files',
                           type=FileStorage, required=True)

UPLOAD_DIR = './uploads'
SCAN_DIR = './scans'


# api for uploading zip file
@api.route('/projects/<int:project_id>/scans/<int:scan_id>/upload')
class ScanResultUpload(Resource):
    @api.expect(upload_parser)
    def post(self, project_id, scan_id):
        scan = Scan.query.filter_by(project_id=project_id, id=scan_id).first_or_404()

        args = upload_parser.parse_args()
        file = args['code']
        stream = args['scan_result']
        os.makedirs(os.path.join(SCAN_DIR, f'{project_id}/{scan_id}'), exist_ok=True)
        stream.save(os.path.join(SCAN_DIR, f'{project_id}/{scan_id}/scan_result.json'))

        os.makedirs(UPLOAD_DIR, exist_ok=True)
        zip_file = os.path.join(UPLOAD_DIR, f'{project_id}-{scan_id}.zip')
        file.save(zip_file)

        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(f'{SCAN_DIR}/{project_id}/{scan_id}/src')

        scan.ready = True
        db.session.commit()

        return {'message': 'File uploaded successfully'}, 202
