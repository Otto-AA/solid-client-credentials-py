def refresh_access_token(previous_token: str | None, dpop_key: str) -> str:
    return "token"


def generate_dpop_key_pair() -> str:
    return "hey"


def create_dpop_header(url: str, method: str, access_token: str) -> str:
    return f"{url}{method}{access_token}"
