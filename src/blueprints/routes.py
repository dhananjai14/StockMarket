from datetime import datetime
from fastapi import APIRouter
from utils.formatting import format_response
from services.mmi_trigger import MMITriggerService
from core_logic.mmi.mmi_provider import MMIDataProvider
from core_logic.alert import NTFYAlert
from utils.logger_config import get_logger
logging = get_logger()

router = APIRouter()


@router.get("/", tags=["health"])
async def index():
    logging.info("Health check endpoint hit.")
    current_time = datetime.now().isoformat()
    response = format_response(
        message="Welcome. Health check successful.",
        data={"server_time": current_time}
    )
    return response


@router.get("/mmi_trigger", tags=["mmi"])
def trigger_mmi():
    logging.info("Inside route /mmi_trigger")
    # Placeholder for MMI trigger logic
    # Creating the dependencies
    mmi_data_provider = MMIDataProvider()
    notification_service = NTFYAlert()

    # Injecting the dependencies into the service
    mmi_trigger_service = MMITriggerService(mmi_data_provider, notification_service)

    message = mmi_trigger_service.trigger_mmi_alert()
    
    # Formatting the response
    response = format_response(
        message="/mmi_trigger endpoint hit.",
        data={"status": message.get("data")},
        status=message.get('status') #type: ignore
    )
    logging.info("MMI process executed.")
    return response