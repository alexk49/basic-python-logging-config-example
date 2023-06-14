from logging.config import dictConfig
from os import path

# update file names if needed
LOGS_DIR = 'logs'
LOGS_FILE = 'logs.txt'
LOGS_FILE_PATH = path.join(LOGS_DIR, LOGS_FILE)

# configire logs
config_dict = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
            "datefmt": "%B %d, %Y %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGS_FILE_PATH,
            "formatter": "default",
            "mode": 'a',
            # set file size can be modified as needed
            "maxBytes": 100000,  
            # you must have backup count as at least one for rotating file handler to work
            "backupCount": 1,          },
    },
    # update level: "INFO" to the level you need for your application
    "root": {"level": "INFO", "handlers": ["console", "file"]},
}
