import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    GEMINI_3_MODEL = os.environ.get('GEMINI_3_MODEL')
    GEMINI_2_5_MODEL = os.environ.get('GEMINI_2_5_MODEL')
    CHROMIUM_DRIVER_PATH = os.environ.get('CHROMIUM_DRIVER_PATH')
    mmi_relative_html_path = os.path.join("save_web_pages", "mmi.html") 
    HEADLESS = True
    NTFY_url = "check_mmi_status_in_cloud"


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/109.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15"
]

mmi_classifications = {
    "Extreme Fear" : 30,
    "Fear" : 50,
    "Greed" : 70,
    "Extreme Greed" : 100
}