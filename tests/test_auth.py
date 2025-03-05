# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison
import httpx
import requests

from solid_client_credentials import DpopTokenProvider, SolidClientCredentialsAuth
from tests.css_utils import CssAcount, get_client_credentials


def describe_create_auth():
    def can_make_authenticated_request(expect, random_css_account: CssAcount):
        credentials = get_client_credentials(random_css_account)
        issuer = random_css_account.css_base_url

        token_provider = DpopTokenProvider(
            issuer_url=issuer,
            client_id=credentials.client_id,
            client_secret=credentials.client_secret,
        )
        auth = SolidClientCredentialsAuth(token_provider)

        private_url = f"{random_css_account.pod_base_url}profile/"
        res = requests.get(private_url, auth=auth, timeout=5000)
        expect(res.status_code) == 200

    def can_make_request_with_query_param(expect, random_css_account: CssAcount):
        credentials = get_client_credentials(random_css_account)
        issuer = random_css_account.css_base_url

        token_provider = DpopTokenProvider(
            issuer_url=issuer,
            client_id=credentials.client_id,
            client_secret=credentials.client_secret,
        )
        auth = SolidClientCredentialsAuth(token_provider)

        # should remove query params
        # https://datatracker.ietf.org/doc/html/rfc9449#section-4.2
        private_url = f"{random_css_account.pod_base_url}profile/?somekey=removeme"
        res = requests.get(private_url, auth=auth, timeout=5000)
        expect(res.status_code) == 200

    def can_use_httpx(expect, random_css_account: CssAcount):
        credentials = get_client_credentials(random_css_account)
        issuer = random_css_account.css_base_url

        token_provider = DpopTokenProvider(
            issuer_url=issuer,
            client_id=credentials.client_id,
            client_secret=credentials.client_secret,
        )
        auth = SolidClientCredentialsAuth(token_provider)

        private_url = f"{random_css_account.pod_base_url}profile/"
        res = httpx.get(private_url, auth=auth, timeout=5000)  # type: ignore
        expect(res.status_code) == 200
