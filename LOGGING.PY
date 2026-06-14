import logging

logging.warning("Program started")
logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Program started")
logging.warning("Low memory")
logging.error("API failed")

print("Done")


import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

try:
    x = 10 / 0

except Exception as e:
    logging.error(e)




import logging
import requests

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Calling GitHub API")

response = requests.get(
    "https://api.github.com"
)

logging.info(response.status_code)

print("Done")