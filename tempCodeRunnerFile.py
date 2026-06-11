import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

try:
    x = 10 / 0

except Exception as e:
    logging.error(e)