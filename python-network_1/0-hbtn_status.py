import requests


def get_status():
    """Gets the status of the HTB intranet."""
    response = requests.get("https://alu-intranet.hbtn.io/status")
    if response.status_code == 200:
        return response.content
    else:
        return None


def main():
    """Prints the body of the response."""
    body = get_status()
    if body:
        print("Body response:\n")
        for key, value in body.items():
            print(f"  - {key}: {value}")
    else:
        print("No status information available.")


if __name__ == "__main__":
    main()
