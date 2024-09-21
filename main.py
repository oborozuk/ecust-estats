import logging
import os
import re
import time

import requests


URL = os.environ.get("URL")


def get_remain_data(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 15; OPPO A5) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36 MicroMessenger/9.0",
    }
    response = requests.get(url, headers=header)
    try:
        remain = float(re.findall(r"(\d+(\.\d+)?)度", response.text)[0][0])
    except:
        remain = -1
        logging.warning("Failed to get data.")
    return remain


def append_to_data_js():
    timestamp = int(time.time())
    remain = get_remain_data(URL)

    file_name = "data.js"

    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("let degreeData = [\n];")

    with open(os.path.join(os.path.dirname(__file__), file_name), "r+") as f:
        content = f.read()
        if not content:
            content = "let degreeData = [\n];"
        new_data = f"    [{timestamp}, {remain}],\n"
        logging.info(timestamp, remain)
        content = content.replace("];", new_data + "];")

        f.seek(0)
        f.write(content)


if __name__ == "__main__":
    try:
        append_to_data_js()
        logging.info("Data appended.")
    except Exception as e:
        logging.error(f"Error: {e}")
