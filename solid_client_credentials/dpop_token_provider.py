from typing import Optional

from solid_client_credentials.access_token import AccessToken
from solid_client_credentials.dpop_utils import (
    create_dpop_header,
    generate_dpop_key_pair,
    refresh_access_token,
)


class DpopTokenProvider:
    def __init__(
        self,
        token_endpoint: str,
        client_id: str,
        client_secret: str,
        refresh_before_expiration_seconds=10,
    ) -> None:
        self._token_endpoint = token_endpoint
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token: Optional[AccessToken] = None
        self._dpop_key = generate_dpop_key_pair()
        self._refresh_before_expiration_seconds = refresh_before_expiration_seconds

    def get_uptodate_access_token(self) -> str:
        self._access_token = refresh_access_token(
            self._token_endpoint,
            self._access_token,
            self._client_id,
            self._client_secret,
            self._dpop_key,
            self._refresh_before_expiration_seconds,
        )

        return self._access_token.value

    def get_dpop_header(self, url: str, method: str) -> str:
        return create_dpop_header(url, method, self._dpop_key)
