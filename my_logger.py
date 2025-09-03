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


def extract_errors(log_file):
    errors = []
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line.upper():
                errors.append(line.strip())
    return errors
