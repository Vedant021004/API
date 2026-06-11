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