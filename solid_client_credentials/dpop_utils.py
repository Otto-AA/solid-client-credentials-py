from jwcrypto import jwk
import jwt

SIGNING_ALG = "ES256"


def generate_dpop_key_pair() -> jwk.JWK:
    key = jwk.JWK.generate(kty="EC", crv="P-256")
    return key


def refresh_access_token(previous_token: str | None, dpop_key: str) -> str:
    return "token"


def create_dpop_header(url: str, method: str, access_token: str) -> str:
    return f"{url}{method}{access_token}"


def jwt_encode(payload: dict, key: jwk.JWK) -> str:
    key_pem = key.export_to_pem(private_key=True, password=None).decode("utf-8")
    encoded_jwt = jwt.encode(payload, key=key_pem, algorithm=SIGNING_ALG)
    return encoded_jwt


def jwt_decode(encoded_jwt: str, key: jwk.JWK) -> dict:
    key_pem = key.export_to_pem(private_key=False, password=None)
    return jwt.decode(encoded_jwt, key=key_pem, algorithms=[SIGNING_ALG])
