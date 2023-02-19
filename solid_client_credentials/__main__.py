#!/usr/bin/env python

"""Package entry point."""
import sys

import requests

from solid_client_credentials import SolidClientCredentialsAuth, DpopTokenProvider


def main():
    issuer_url = sys.argv[1]
    client_id = sys.argv[2]
    client_secret = sys.argv[3]
    url = sys.argv[4]

    token_provider = DpopTokenProvider(
        issuer_url=issuer_url, client_id=client_id, client_secret=client_secret
    )
    auth = SolidClientCredentialsAuth(token_provider)

    res_no_auth = requests.get(url, timeout=5000)
    print(f"without authentication: {res_no_auth}")
    res_auth = requests.get(url, auth=auth, timeout=5000)
    print(f"with authentication: {res_auth}")
    print(res_auth.text)


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
