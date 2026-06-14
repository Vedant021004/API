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