# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison
import requests

from solid_client_credentials import SolidClientCredentialsAuth
from tests.css_utils import CssAcount, get_client_credentials


def describe_create_auth():
    def can_make_authenticated_request(expect, random_css_account: CssAcount):
        token_endpoint = f"{random_css_account.css_base_url}/.oidc/token"
        credentials = get_client_credentials(random_css_account)

        auth = SolidClientCredentialsAuth(
            token_endpoint=token_endpoint,
            client_id=credentials.client_id,
            client_secret=credentials.client_secret,
        )

        private_url = f"{random_css_account.pod_base_url}profile/"
        res = requests.get(private_url, auth=auth, timeout=5000)
        expect(res.status_code) == 200
