"""Create an application instance."""
import os

from notifyme.app import create_app
from notifyme.config import DevelopmentConfig

app_config = os.getenv('APP_CONFIG', DevelopmentConfig)
app = create_app(config_object=app_config)
