import logging

from config_dict import config_dict

logging.config.dictConfig(config_dict)

name = input("What's your name? ")

if name == "":
    logging.critical("No input given")
else:
    logging.info("Name given as: %s", name)
    print(f"Hi {name}")
