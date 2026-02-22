from flask import Flask
from config import Config
from models.models import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS  # 1. Import CORS
from routes.auth import auth_bp
from routes.university import university_bp
from routes.employer import employer_bp
from routes.applicant import applicant_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app) # 2. Enable CORS for all routes
    
    db.init_app(app)
    JWTManager(app)

    # Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(university_bp, url_prefix='/university')
    app.register_blueprint(employer_bp, url_prefix='/employer')
    app.register_blueprint(applicant_bp, url_prefix='/applicant')

    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)