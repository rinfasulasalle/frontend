import os
from   flask_migrate import Migrate
from   flask_minify  import Minify
from   sys import exit
from flask_cors import CORS

from apps.config import config_dict
from apps import create_app, db

DEBUG = (os.getenv('DEBUG', 'True') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
CORS(app, resources={r"/trabajador/*": {"origins": "http://127.0.0.1:5050"}})  # Especifica el origen permitido para las rutas de /trabajador

Migrate(app, db)

if not DEBUG:
    Minify(app=app, html=True, js=True, cssless=True)

if __name__ == "__main__":
    app.run(port=5050)
