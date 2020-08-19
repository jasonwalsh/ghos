import requests

METHOD_GET = "GET"
METHOD_PUT = "PUT"


class Client:
    def __init__(
        self, endpoint: str = "api.github.com", organization: str = "", token: str = ""
    ):
        self.endpoint = endpoint
        self.organization = organization
        session = requests.Session()
        session.headers["Accept"] = "application/vnd.github.v3+json"
        session.headers["Authorization"] = f"token {token}"
        self.session = session

    def create_secret(self, secret_name: str, encrypted_value: str, key_id: str):
        """Creates an organization secret with an encrypted value."""
        url = f"/orgs/{self.organization}/actions/secrets/{secret_name}"
        data = {
            "encrypted_value": encrypted_value,
            "key_id": key_id,
            "visibility": "all",
        }
        return self.request(METHOD_PUT, url, body=data)

    def get_public_key(self):
        """Gets your public key, which you need to encrypt secrets."""
        url = f"/orgs/{self.organization}/actions/secrets/public-key"
        return self.request(METHOD_GET, url)

    def request(self, method: str, url: str, body=None):
        url = f"https://{self.endpoint}{url}"
        return self.session.request(method, url, json=body)
