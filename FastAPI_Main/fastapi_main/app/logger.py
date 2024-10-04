from loguru import logger

# Configure logger settings
logger.add("app.log", rotation="1 MB", retention="7 days", level="INFO")

# This log configuration writes logs to app.log file and rotates them when they exceed 1MB.