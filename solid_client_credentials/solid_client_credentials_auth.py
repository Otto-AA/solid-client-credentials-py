from requests.auth import AuthBase
from requests.models import PreparedRequest

from solid_client_credentials.dpop_token_provider import DpopTokenProvider


class SolidClientCredentialsAuth(AuthBase):
    def __init__(self, dpop_token_provider: DpopTokenProvider) -> None:
        self._token_provider = dpop_token_provider

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        method = r.method or "GET"
        if not r.url:
            raise Exception(f"Unexpected request without url: {r}")

        # for httpx, r.url is an URL object and not a string
        # so we convert it here
        url = str(r.url)

        access_token = self._token_provider.get_uptodate_access_token()
        dpop_header = self._token_provider.get_dpop_header(url, method)

        r.headers["Authorization"] = f"DPoP {access_token}"
        r.headers["DPoP"] = dpop_header

        return r
