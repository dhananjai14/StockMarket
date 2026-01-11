import traceback
from typing import Dict, Any
from utils.logger_config import get_logger
logging = get_logger()


class MMITriggerService:
    """
    Service to handle MMI trigger service implementation.
    Idea: Create a trigger to mobile as soon as the MMI reaches in `Extreme Fear` condition.
    """

    def __init__(self, mmi_data_provider, notification_service):
        """
        :param mmi_data_provider: Object with a method (e.g., fetch_mmi_data())
        :param notification_service: Object with a method (e.g., send_alert())
        """
        self.mmi_data_provider = mmi_data_provider
        self.notification_service = notification_service
    
    def trigger_mmi_alert(self) -> Dict[str, Any]:
        """
        Triggers an alert if MMI indicates 'Extreme Fear'.
        """
        logging.info("=========== Inside method: trigger_mmi_alert ===========")
        try:
            mmi_data = self.mmi_data_provider.fetch_mmi_data()
            logging.info(f"Fetched MMI Data: {mmi_data}")
            if mmi_data.get('market_mood_index') == 'Extreme Fear':
                alert_message = f"Alert: Market Mood Index is at Extreme Fear ({mmi_data.get('value')}). Consider reviewing your portfolio."
                self.notification_service.send_alert(alert_message)
                logging.info("Extreme Fear alert sent successfully.")
            else:
                logging.info("Market Mood Index is not at Extreme Fear. No alert sent.")
            return {"status": 200, "data": mmi_data}
        except Exception as e:
            detailed_error = traceback.format_exc()
            logging.error(f"Error in [trigger_mmi_alert]: {detailed_error}")
            return {"status": 500, "data": str(e)}
    
    
