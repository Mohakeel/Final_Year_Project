from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.models import db, Job, VerificationRequest, Employer
from utils.decorators import role_required

employer_bp = Blueprint('employer', __name__)

@employer_bp.route('/jobs', methods=['POST'])
@jwt_required()
@role_required('employer')
def create_job():
    data = request.get_json()
    user_id = get_jwt_identity()
    employer = Employer.query.filter_by(user_id=user_id).first()
    
    new_job = Job(
        employer_id=employer.id,
        title=data['title'],
        description=data['description']
    )
    db.session.add(new_job)
    db.session.commit()
    return jsonify({"message": "Job posted successfully"}), 201

@employer_bp.route('/request-verification', methods=['POST'])
@jwt_required()
@role_required('employer')
def request_verification():
    data = request.get_json()
    user_id = get_jwt_identity()
    employer = Employer.query.filter_by(user_id=user_id).first()
    
    new_request = VerificationRequest(
        employer_id=employer.id,
        university_id=data['university_id'],
        student_name=data['student_name'],
        degree=data['degree'],
        year=data['year'],
        status='PENDING'
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({"message": "Verification request sent to University"}), 201