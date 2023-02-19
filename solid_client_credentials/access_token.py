import datetime


class AccessToken:
    def __init__(self, token: str, expiration: datetime.datetime) -> None:
        self.value = token
        self.expiration = expiration

    def is_expired(self) -> bool:
        return self.expiration < datetime.datetime.now()
