from solid_client_credentials import SolidClientCredentialsAuth


def describe_create_auth():
    def when_no_params(expect):
        SolidClientCredentialsAuth(client_id="me", client_secret="abc123")
