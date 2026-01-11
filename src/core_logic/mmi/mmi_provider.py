import os 
import asyncio
import random
import traceback
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from config import Config, user_agents, mmi_classifications
from utils.logger_config import get_logger
logging = get_logger()

CHROMIUM_DRIVER_PATH = Config.CHROMIUM_DRIVER_PATH


class MMIDataProvider:
    """
    Provides functionality to fetch Market Mood Index (MMI) data.
    """
    def __init__(self):
        self.chromium_path = CHROMIUM_DRIVER_PATH

    async def get_mmi(self):
        """
        Main business logic: checks data and triggers alert if 'Extreme Fear'.
        """
        logging.info("=========== Inside method: get_mmi ===========")
        try:
            async with Stealth().use_async(async_playwright()) as p:
                browser = await p.chromium.launch(headless=Config.HEADLESS,
                                                args=[
                                                    "--disable-blink-features=AutomationControlled",
                                                    "--no-sandbox",
                                                    "--disable-dev-shm-usage"
                                                        ],
                                                executable_path=CHROMIUM_DRIVER_PATH)
                context = await browser.new_context(
                    user_agent=random.choice(user_agents),
                    viewport={"width": 1280, "height": 800}
                )
                page = await context.new_page()
                await page.goto("https://www.tickertape.in/market-mood-index?ref=homepage_mmi_section")
                await page.wait_for_timeout(500)  # Wait for JS to load content (adjust as needed)
                await page.evaluate("""
                                () => {
                                    window.scrollTo(0, document.body.scrollHeight);
                                }
                        """)

                html = await page.content()
                cwd = os.getcwd()
                save_dir = os.path.join(cwd, Config.mmi_relative_html_path)
                # Check if the directory exists, if not, create it
                os.makedirs(os.path.dirname(save_dir), exist_ok=True)

                logging.info(f"Saving MMI data to {save_dir}")
                with open(save_dir, "w", encoding="utf-8") as f:
                    f.write(html)
                await browser.close()
                logging.info("MMI page saved successfully.")

        except Exception as e:
            detailed_error = traceback.format_exc()
            logging.error(f"Error in [get_mmi]: {detailed_error}")
            raise e


    def fetch_mmi_data(self):
        """
        Fetches MMI data by running the async get_mmi method.
        """
        logging.info("=========== Inside method: fetch_mmi_data ===========")
        try:
            asyncio.run(self.get_mmi())
            cwd = os.getcwd()
            mmi_html_path = os.path.join(cwd, Config.mmi_relative_html_path)
            if not os.path.exists(mmi_html_path):
                logging.info("MMI HTML file does not exist. Please run the save_mmi_data function first.")
                raise FileNotFoundError("MMI HTML file does not exist. Please run the save_mmi_data function first.")
            with open(mmi_html_path, "r", encoding="utf-8") as f:
                mmi_html = f.read()
            mmi_soup = BeautifulSoup(mmi_html, "html.parser")
            MMI = mmi_soup.select('span[class^="jsx-3654585993"]')[0].get_text(strip=True)

            mmi_value = float(MMI)
            mood_category = "Unknown" 
            for key, value in mmi_classifications.items():
                if mmi_value < value:
                    mood_category = key
                    break
            mmi_data = {
                'market_mood_index': mood_category,
                'value': MMI
            }
            logging.info(f"Extracted MMI: {MMI}, Market Mood Index: {mood_category}")

            return mmi_data
        except Exception as e:
            detailed_error = traceback.format_exc()
            logging.error(f"Error in [fetch_mmi_data]: {detailed_error}")
            raise e


if __name__ == "__main__":
    # Sample usage
    mmi_provider = MMIDataProvider()
    mmi_data = mmi_provider.fetch_mmi_data()
    print(f"MMI Data: {mmi_data}")