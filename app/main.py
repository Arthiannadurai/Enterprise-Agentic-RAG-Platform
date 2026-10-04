
print("its working", __name__)
from app.config import APP_NAME,GEMINI_MODEL
from app.logger import get_logger
logger = get_logger(__name__)

def main()->None:
    logger.info("Application starting")
    logger.info("Application name: %s", APP_NAME)
    logger.info("Configured model: %s", GEMINI_MODEL)
    logger.info("Project setup completed")

if __name__ == "__main__":
    main()
