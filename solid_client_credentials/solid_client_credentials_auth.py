from typing import Optional

from requests.auth import AuthBase
from requests.models import PreparedRequest

from solid_client_credentials.dpop_utils import (
    create_dpop_header,
    generate_dpop_key_pair,
    refresh_access_token,
)


class SolidClientCredentialsAuth(AuthBase):
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token: Optional[str] = None

        self.dpop_key = generate_dpop_key_pair()

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        self.access_token = refresh_access_token(self.access_token, self.dpop_key)

        method = r.method or "GET"
        url = r.url or "TODO"

        dpop_header = create_dpop_header(url, method, self.access_token)
        r.headers["Authorization"] = f"DPoP {self.access_token}"
        r.headers["DPoP"] = dpop_header
        print(self.client_id)
        return r
