import os

class Config:
    SECRET_KEY = 'your-secret-key' # Change this for production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'jwt-secret-key'
    UPLOAD_FOLDER = 'uploads/resumes'