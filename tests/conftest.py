"""Integration tests configuration file."""

# pylint: disable=unused-import
import log
import pytest
import requests

from solid_client_credentials.tests.conftest import pytest_configure

from .css_utils import given_random_account


def css_is_responsive(url):
    try:
        return requests.get(url, timeout=1000).status_code == 200
    except ConnectionError:
        print("err")
        return False
    except Exception:
        return False


@pytest.fixture(scope="session")
def community_solid_server_url(docker_services):
    """Ensure that the CommunitySolidServer is up and responsive."""

    port = docker_services.port_for("css", 3000)
    # we use localhost because CSS requires either https or localhost
    # with 127.0.0.1 (coming from docker_ip) it rejects because of insecurity
    url = f"http://localhost:{port}"
    log.debug(f"waiting for CSS to come online at {url}")
    docker_services.wait_until_responsive(
        timeout=120.0, pause=0.1, check=lambda: css_is_responsive(url)
    )
    log.debug(f"CSS started at {url}")
    return url


@pytest.fixture()
def random_css_account(community_solid_server_url: str):
    return given_random_account(community_solid_server_url)
