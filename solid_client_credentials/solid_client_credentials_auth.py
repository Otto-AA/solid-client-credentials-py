from typing import Optional

import log
from requests.auth import AuthBase
from requests.models import PreparedRequest

from solid_client_credentials.access_token import AccessToken
from solid_client_credentials.dpop_utils import (
    create_dpop_header,
    generate_dpop_key_pair,
    refresh_access_token,
)


class SolidClientCredentialsAuth(AuthBase):
    def __init__(self, token_endpoint: str, client_id: str, client_secret: str) -> None:
        self.token_endpoint = token_endpoint
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token: Optional[AccessToken] = None

        self.dpop_key = generate_dpop_key_pair()

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        self.access_token = refresh_access_token(
            self.token_endpoint,
            self.access_token,
            self.client_id,
            self.client_secret,
            self.dpop_key,
        )

        method = r.method or "GET"
        if not r.url:
            raise Exception(f"Unexpected request without url: {r}")

        dpop_header = create_dpop_header(r.url, method, self.dpop_key)
        log.debug(f"adding dpop header for {r.url}: {dpop_header}")
        r.headers["Authorization"] = f"DPoP {self.access_token.value}"
        r.headers["DPoP"] = dpop_header

        return r
