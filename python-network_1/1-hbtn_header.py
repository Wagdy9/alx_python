#!/usr/bin/env python3
import requests
import sys

url = sys.argv[1]

response = requests.get(url)
print(response.headers["X-Request-Id"])