# Solid Client Credentials

Solid authentication with client credentials.

[![Unix Build Status](https://img.shields.io/github/actions/workflow/status/Otto-AA/solid-client-credentials-py/main.yml?branch=main&label=linux)](https://github.com/Otto-AA/solid-client-credentials-py/actions)
[![Coverage Status](https://img.shields.io/codecov/c/gh/Otto-AA/solid-client-credentials-py)](https://codecov.io/gh/Otto-AA/solid-client-credentials-py)
[![PyPI License](https://img.shields.io/pypi/l/SolidClientCredentials.svg)](https://pypi.org/project/SolidClientCredentials)
[![PyPI Version](https://img.shields.io/pypi/v/SolidClientCredentials.svg)](https://pypi.org/project/SolidClientCredentials)
[![PyPI Downloads](https://img.shields.io/pypi/dm/SolidClientCredentials.svg?color=orange)](https://pypistats.org/packages/SolidClientCredentials)

## Setup

### Requirements

* Python 3.10+ (likely works with lower versions, but not tested)

### Installation

```bash
$ pip install SolidClientCredentials
```

## Use Case

!!! note
    Client credentials are not standardized, thus you can't run your application through any Solid pod. However, users from any provider can give your app access through standardized mechanisms (eg ACL).


You can use client credentials to create a server-side application that authenticates as a webId on ESS or CSS. After obtaining the client credentials for a webId, you can use them to make authenticated requests on behalf of this account. You will be able to access all resources this webId has access to. If you want to access data of other users, they must grant access rights to your apps webId.

See also: [https://docs.inrupt.com/developer-tools/javascript/client-libraries/tutorial/authenticate-nodejs-script/](https://docs.inrupt.com/developer-tools/javascript/client-libraries/tutorial/authenticate-nodejs-script/)

## Usage

To use this package you first need valid client credentials (see [below](#obtaining-client-credentials)). Given the client credentials you can use it as follows:

```python
from solid_client_credentials import SolidClientCredentialsAuth, DpopTokenProvider
import requests

client_id = 'your-id'
client_secret = 'your-secret'

# The server that provides your account (where you login)
issuer_url = 'https://login.inrupt.com'

# create a token provider
token_provider = DpopTokenProvider(
    issuer_url=issuer_url,
    client_id=client_id,
    client_secret=client_secret
)
# use the tokens with the requests library
auth = SolidClientCredentialsAuth(token_provider)

res = requests.get('https://example.org/private/stuff', auth=auth)
print(res.text)
```

## Obtaining client credentials

This is currently only possible with ESS and CSS.

### ESS

ESS allows to manually obtain client credentials: [https://login.inrupt.com/registration.html](https://login.inrupt.com/registration.html)

### CSS

CSS allows to automatically obtain client credentials: [https://communitysolidserver.github.io/CommunitySolidServer/5.x/usage/client-credentials/](https://communitysolidserver.github.io/CommunitySolidServer/5.x/usage/client-credentials/)

You can also look at `css_utils.py` to see how this maps to python.

