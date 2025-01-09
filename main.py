import re
import requests
import os
import time


URL = os.environ.get("URL", "").strip()
PUSH_PLUS_TOKEN = os.environ.get("PUSH_PLUS_TOKEN", "").strip()


def get_degree(url, retry=3):
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 15; OPPO A5) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36 MicroMessenger/9.0",
    }
    try:
        response = requests.get(url, headers=header)
        return float(re.findall(r"(\d+(\.\d+)?)度", response.text)[0][0])
    except Exception as e:
        if retry > 0:
            time.sleep(1)
            return get_degree(url, retry - 1)
        else:
            print(f"Failed to get data. {e}")
        return -1


def append_to_data_js(timestamp, degree):
    file_path = os.path.join(os.path.dirname(__file__), "data.js")

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("let degreeData = [\n];")

    with open(file_path, "r+") as f:
        content = f.read()
        new_data = f"    [{timestamp}, {degree}],\n"
        content = content.replace("];", new_data + "];")

        f.seek(0)
        f.write(content)


def send_warning(degree):
    import json

    if not PUSH_PLUS_TOKEN:
        return

    url = "http://www.pushplus.plus/send"

    if degree <= 5:
        title = "宿舍剩余电量低于 5 度"
    elif degree <= 10:
        title = "宿舍剩余电量低于 10 度"
    text = f"当前剩余电量为 {degree} 度，请及时[充值]({URL})。\n[查看详情](https://estats.2124096.xyz/)"
    data = {
        "token": PUSH_PLUS_TOKEN,
        "title": title,
        "content": text,
        "template": "markdown",
    }
    requests.post(url=url, data=(json.dumps(data).encode(encoding="utf-8")), timeout=20)


if __name__ == "__main__":
    if not URL:
        print("Please set the URL environment variable.")
        exit(1)
    try:
        timestamp = int(time.time())
        degree = get_degree(URL)
        append_to_data_js(timestamp, degree)
        print(f"Data appended. ({timestamp}, {degree})")
        if 0 <= degree <= 10:
            send_warning(degree)
    except Exception as e:
        print(f"Error: {e}")
