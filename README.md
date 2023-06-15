# Python Logging Config

This is a easily portable standard logging config to be used with simple python applications. It writes logs to both the console and to a file, and is easily modifiable to the needs of your application. By default the logs are saved in a directory called logs so you must make this before running.

To use with your project, you just need to save the config_dict.py file in your project folder and import it with:

```
# import logging module
import logging
# local file import
from config_dict import config_dict

# set logs to use config
logging.config.dictConfig(config_dict)
```

Once this has been done, you can write logs with:

```
logging.info("Logging message")
logging.info("Logging message with variable: %s", example_variable)
```

Updating the logging level as required.
