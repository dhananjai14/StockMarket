import os
from src import create_app
from dotenv import load_dotenv
from src.utils.logger_config import get_logger

logging = get_logger()
load_dotenv()

config_name = os.getenv('FLASK_ENV') or 'default'
logging.info(f"Starting application with config: {config_name}")
app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)