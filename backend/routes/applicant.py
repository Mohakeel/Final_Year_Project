import os
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.models import db, Applicant, Job
from utils.decorators import role_required
from werkzeug.utils import secure_filename

applicant_bp = Blueprint('applicant', __name__)

@applicant_bp.route('/upload-resume', methods=['POST'])
@jwt_required()
@role_required('applicant')
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['resume']
    user_id = get_jwt_identity()
    applicant = Applicant.query.filter_by(user_id=user_id).first()
    
    if file:
        filename = secure_filename(f"user_{user_id}_{file.filename}")
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        applicant.resume_path = file_path
        db.session.commit()
        return jsonify({"message": "Resume uploaded successfully", "path": file_path}), 200

@applicant_bp.route('/view-jobs', methods=['GET'])
@jwt_required()
def get_jobs():
    jobs = Job.query.all()
    output = []
    for job in jobs:
        output.append({"id": job.id, "title": job.title, "description": job.description})
    return jsonify(output), 200