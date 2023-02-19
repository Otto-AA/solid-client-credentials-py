from importlib.metadata import PackageNotFoundError, version

from .solid_client_credentials_auth import SolidClientCredentialsAuth
from .dpop_token_provider import DpopTokenProvider
from .access_token import AccessToken

try:
    __version__ = version("SolidClientCredentials")
except PackageNotFoundError:
    __version__ = "(local)"

del PackageNotFoundError
del version
