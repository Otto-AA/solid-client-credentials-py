"""Sample unit test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import datetime
from solid_client_credentials import dpop_utils
from solid_client_credentials.access_token import AccessToken


def describe_generate_dpop_key_pair():
    def creates_ecdsa256_key_pair(expect):
        key = dpop_utils.generate_dpop_key_pair()
        key_export: dict = key.export(as_dict=True)
        expect(key_export["kty"]) == "EC"
        expect(key_export["crv"]) == "P-256"
        expect(key_export["x"]).isinstance(str)
        expect(key_export["y"]).isinstance(str)


def describe_jwt_signing():
    def signs_jwt(expect):
        key = dpop_utils.generate_dpop_key_pair()
        jwt = dpop_utils.jwt_encode({"test": True}, key, headers={"foo": "bar"})
        expect(jwt).isinstance(str)

    def decodes_jwt_headers(expect):
        key = dpop_utils.generate_dpop_key_pair()
        jwt = dpop_utils.jwt_encode({"test": True}, key, headers={"foo": "bar"})
        original = dpop_utils.jwt_decode_without_verification(jwt)
        expect(original["test"]) == True


def describe_access_token():
    def creates_token_if_none(expect, mocker):
        mocker.patch("solid_client_credentials.dpop_utils.request_access_token")

        dpop_utils.refresh_access_token(
            "", None, "client-1", "secret-1", "fake key", 10
        )

        dpop_utils.request_access_token.assert_called_once()  # pylint: disable=E1101

    def returns_token_if_valid(expect, mocker):
        refresh_before_expiration_s = 10
        token = AccessToken(
            "token", datetime.datetime.now() + datetime.timedelta(seconds=60)
        )

        result = dpop_utils.refresh_access_token(
            "", token, "client-1", "secret-1", "fake key", refresh_before_expiration_s
        )

        expect(result) == token

    def creates_token_if_token_expired_before_now(mocker):
        mocker.patch("solid_client_credentials.dpop_utils.request_access_token")
        refresh_before_expiration_s = 10
        token = AccessToken(
            "token", datetime.datetime.now() - datetime.timedelta(seconds=60)
        )

        dpop_utils.refresh_access_token(
            "", token, "client-1", "secret-1", "fake key", refresh_before_expiration_s
        )

        dpop_utils.request_access_token.assert_called_once()  # pylint: disable=E1101

    def creates_token_if_token_expires_within_threshold(mocker):
        mocker.patch("solid_client_credentials.dpop_utils.request_access_token")
        refresh_before_expiration_s = 10
        token = AccessToken(
            "token", datetime.datetime.now() + datetime.timedelta(seconds=5)
        )

        dpop_utils.refresh_access_token(
            "", token, "client-1", "secret-1", "fake key", refresh_before_expiration_s
        )

        dpop_utils.request_access_token.assert_called_once()  # pylint: disable=E1101
