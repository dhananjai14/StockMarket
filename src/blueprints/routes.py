from datetime import datetime
from flask import jsonify
from flask import Blueprint
from src.utils.formatting import format_response
from src.utils.logger_config import get_logger
logging = get_logger()

health_check = Blueprint('health_check', __name__)
@health_check.route('/', methods=['GET'])
def index():
    logging.info("Health check endpoint hit.")
    # Use the Service layer for logic
    current_time = datetime.now()
    
    # Use the Utils layer for formatting
    response = format_response(
        message="Welcome. Health check successful.",
        data={"server_time": current_time}
    )
    return jsonify(response)

