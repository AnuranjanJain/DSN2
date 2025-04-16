import os
from datetime import timedelta

# Base configuration
class Config:
    # Application settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-for-dev-only'
    DEBUG = False
    TESTING = False
    
    # Session settings
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # Database settings (MySQL)
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or 'password'
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'cardio_guide'
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT') or 3306)
    
    # Mail settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

# Development configuration
class DevelopmentConfig(Config):
    DEBUG = True
    
    # Override for development
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or 'dev_password'
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'cardio_guide_dev'

# Testing configuration
class TestingConfig(Config):
    TESTING = True
    
    # Use a test database
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'cardio_guide_test'

# Production configuration 
class ProductionConfig(Config):
    # Production should use environment variables
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # TLS/SSL settings
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# Model configuration
MODEL_CONFIG = {
    'model_path': 'models/framingham_model.pkl',
    'dataset_path': 'framingham.csv',
    'feature_mapping': {
        'male': 'gender',
        'age': 'age',
        'education': 'education',
        'currentSmoker': 'current_smoker',
        'cigsPerDay': 'cigs_per_day',
        'BPMeds': 'bp_meds',
        'prevalentStroke': 'prevalent_stroke',
        'prevalentHyp': 'prevalent_hyp',
        'diabetes': 'diabetes',
        'totChol': 'tot_chol',
        'sysBP': 'sys_bp',
        'diaBP': 'dia_bp',
        'BMI': 'bmi',
        'heartRate': 'heart_rate',
        'glucose': 'glucose',
        'TenYearCHD': 'target'
    }
}