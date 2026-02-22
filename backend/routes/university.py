from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.models import db, VerificationRequest
from utils.helpers import generate_hash  # <--- Ensure this matches now
from utils.decorators import role_required

university_bp = Blueprint('university_bp', __name__)

@university_bp.route('/verify-request/<int:request_id>', methods=['POST'])
@jwt_required()
@role_required('university')
def verify_certificate(request_id):
    data = request.get_json()
    status = data.get('status')
    req = VerificationRequest.query.get_or_404(request_id)

    if status == 'VERIFIED':
        # Ensure the function call matches the import
        cert_hash = generate_hash(req.student_name, "University Name", req.degree, req.year)
        req.status = 'VERIFIED'
        req.cert_hash = cert_hash
    else:
        req.status = 'REJECTED'
        req.rejection_reason = data.get('reason')

    db.session.commit()
    return jsonify({"message": "Verification processed", "hash": req.cert_hash}), 200