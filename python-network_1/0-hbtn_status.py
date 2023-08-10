"""This module fetches the status of the HTB intranet and prints the body of the response."""

import requests


def get_status():
    response = requests.get("https://intranet.hbtn.io/status")
    content = response.content.decode("utf-8")
    return content


if __name__ == "__main__":
    print("Body response:")
    print("\t- type: {_type}".format(_type=type(content)))
    print("\t- content: {_content}".format(_content=content))
    print("\t- utf8 content: {_utf8_c}".format(_utf8_c=content))

print(get_status())
