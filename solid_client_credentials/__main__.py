#!/usr/bin/env python

"""Package entry point."""
import sys

import requests

from solid_client_credentials import SolidClientCredentialsAuth


def main():
    token_endpoint = sys.argv[1]
    client_id = sys.argv[2]
    client_secret = sys.argv[3]
    url = sys.argv[4]

    auth = SolidClientCredentialsAuth(
        token_endpoint=token_endpoint, client_id=client_id, client_secret=client_secret
    )

    res_no_auth = requests.get(url, timeout=5000)
    print(res_no_auth)
    res_auth = requests.get(url, auth=auth, timeout=5000)
    print(res_auth)
    print(res_auth.text)


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
