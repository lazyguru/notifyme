"""Application configuration."""
import logging
import os
from os.path import join, dirname
from dotenv import load_dotenv


class Config(object):
    """Base configuration."""

    # Create .env file path.
    dotenv_path = join(dirname(dirname(__file__)), '.env')

    # Load file from the path.
    load_dotenv(dotenv_path)

    SECRET_KEY = os.environ.get('NOTIFYME_SECRET', 'default-secret-key')
    NEXMO_KEY = os.environ.get('NOTIFYME_NEXMO_KEY', '')
    NEXMO_SECRET = os.environ.get('NOTIFYME_NEXMO_SECRET', '')
    NEXMO_FROM = os.environ.get('NOTIFYME_NEXMO_FROM', '')
    NEXMO_TO = os.environ.get('NOTIFYME_NEXMO_TO', '')


class DevelopmentConfig(Config):
    """Development configuration."""

    ENV = 'development'
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class TestingConfig(Config):
    """Test configuration."""

    ENV = 'testing'
    DEBUG = True
    TESTING = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """Production configuration."""

    ENV = 'production'
    DEBUG = False
    TESTING = False
    URL_PREFIX = os.environ.get('NOTIFYME_URL_PREFIX',
                                '/notifyme')
    LOG_LEVEL = logging.WARNING
