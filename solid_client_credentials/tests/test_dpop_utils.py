"""Sample unit test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from solid_client_credentials import dpop_utils


def describe_generate_dpop_key_pair():
    def creates_ecdsa256_key_pair(expect):
        key = dpop_utils.generate_dpop_key_pair()
        key_export: dict = key.export(as_dict=True)
        expect(key_export["kty"]) == "EC"
        expect(key_export["crv"]) == "P-256"
        expect(key_export["x"]).isinstance(str)
        expect(key_export["y"]).isinstance(str)


def describe_jwt_signing():
    def can_sign_jwt(expect):
        key = dpop_utils.generate_dpop_key_pair()
        jwt = dpop_utils.jwt_encode({"test": True}, key)
        expect(jwt).isinstance(str)

    def can_verify_jwt(expect):
        key = dpop_utils.generate_dpop_key_pair()
        jwt = dpop_utils.jwt_encode({"test": True}, key)
        original = dpop_utils.jwt_decode(jwt, key)
        expect(original["test"]) == True
