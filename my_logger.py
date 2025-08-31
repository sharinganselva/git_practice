import logging

# Configure logging (write to file + console)
logging.basicConfig(
    level=logging.INFO,
    format="Custom Log: %(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("timings.log"),   # logs to file
        logging.StreamHandler()               # logs to console
    ]
)
