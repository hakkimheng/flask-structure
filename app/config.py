import os


class Config:
    """Base configuration"""
    pass


class DevelopmentConfig(Config):
    """Development configuration"""
    pass


class ProductionConfig(Config):
    """Production configuration"""
    pass


class TestingConfig(Config):
    """Testing configuration"""
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

