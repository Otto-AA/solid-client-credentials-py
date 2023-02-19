# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison
import requests

from solid_client_credentials import SolidClientCredentialsAuth, DpopTokenProvider
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
