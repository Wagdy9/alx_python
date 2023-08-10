"""This module fetches the status of the HTB intranet and prints the body of the response."""

import requests
import json


class HTBStatus:
    """Gets the status of the HTB intranet."""

    def __init__(self):
        """Initializes the HTBStatus object."""
        self.response = requests.get("https://intranet.hbtn.io/status")

    def get_body(self):
        """Gets the body of the response and decodes it as JSON.

        Returns:
          A dictionary containing the response data.
        """
        if self.response.status_code == 200:
            return json.loads(self.response.content.decode())
        else:
            return None


def main():
    """Prints the body of the response."""
    hbtn_status = HTBStatus()
    body = hbtn_status.get_body()
    if body:
        print("Body response:\n")
        for key, value in body.items():
            print(f"  - {key}: {value}")
    else:
        print("No status information available.")


if __name__ == "__main__":
    main()
