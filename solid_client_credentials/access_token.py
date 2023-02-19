import datetime


class AccessToken:
    def __init__(self, token: str, expiration: datetime.datetime) -> None:
        self.value = token
        self.expiration = expiration

    def expires_within(self, seconds: int) -> bool:
        return self.expiration < datetime.datetime.now() + datetime.timedelta(
            seconds=seconds
        )
