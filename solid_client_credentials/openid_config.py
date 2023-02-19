from urllib.parse import urljoin
import requests

WELL_KNOWN_OPENID_CONFIG = ".well-known/openid-configuration"


class OpenIdConfig:
    """Simplified version of OpenId config."""

    def __init__(self, issuer: str, token_endpoint: str) -> None:
        self.issuer = issuer
        self.token_endpoint = token_endpoint

    @staticmethod
    def fetch(issuer: str):
        url = urljoin(issuer, WELL_KNOWN_OPENID_CONFIG)
        res = requests.get(url, timeout=5000)
        data = res.json()
        return OpenIdConfig(issuer=issuer, token_endpoint=data["token_endpoint"])
