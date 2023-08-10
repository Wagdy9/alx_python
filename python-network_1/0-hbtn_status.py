def get_body(self):
    """Gets the body of the response and decodes it as JSON."""
    if self.response.status_code == 200:
        return json.loads(self.response.content.decode())
    else:
        return None
