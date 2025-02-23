import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Settings:
    """Simple configuration class using environment variables."""

    def __init__(self):
        self.MODEL_NAME = os.getenv("MODEL_NAME", "distilbert-base-uncased")
        self.MAX_LENGTH = int(os.getenv("MAX_LENGTH", 128))
        self.PORT = int(os.getenv("PORT", 8000))
        self.HOST = os.getenv("HOST", "0.0.0.0")
        self.ENV = os.getenv("ENV", "development")

        logger.info(f"Loaded config: MODEL_NAME={self.MODEL_NAME}, ENV={self.ENV}")


settings = Settings()