import traceback
import requests
from abc import ABC, abstractmethod
from config import Config
from utils.logger_config import get_logger
logging = get_logger()

class Alert(ABC):
    """
    Abstract base class for alerts. Any alerting mechanism should inherit from this class and implement the send_alert method.
    """

    @abstractmethod
    def send_alert(self, message: str):
        """
        Simulates sending an alert by printing the message to the console.
        :param message: The alert message.

        """
        pass

class NTFYAlert(Alert):
    """
    Concrete implementation of Alert that sends notifications to mobine using the `ntfy` service.
    """

    def send_alert(self, message: str):
        try:
            logging.info("=========== Inside method: send_alert ===========")
            logging.info("Notification sending initiated.")
            print(f"ALERT: {message}")
            requests.post(f"https://ntfy.sh/{Config.NTFY_url}", 
                  data=message.encode(encoding='utf-8'))
            logging.info("Notification sent successfully.")

        except Exception as e:
            detailed_error = traceback.format_exc()
            logging.error(f"Error in [send_alert]: {detailed_error}")
            raise e
        

if __name__ == "__main__":
    # Sample usage
    alert = NTFYAlert()
    alert.send_alert("This is a test alert.")