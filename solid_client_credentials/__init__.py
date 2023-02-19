from importlib.metadata import PackageNotFoundError, version

from .access_token import AccessToken
from .dpop_token_provider import DpopTokenProvider
from .solid_client_credentials_auth import SolidClientCredentialsAuth

try:
    __version__ = version("SolidClientCredentials")
except PackageNotFoundError:
    __version__ = "(local)"

del PackageNotFoundError
del version
