import os
import uvicorn
from src import create_app
from dotenv import load_dotenv
from src.utils.logger_config import get_logger

logging = get_logger()
load_dotenv()

app = create_app()

if __name__ == '__main__':
    # uvicorn.run(app, host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", 8000)), reload=True)
    uvicorn.run("app:app", host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", 8000)), reload=True)