import pytest

from stamphq.client import StampHQClient

DEFAULT_API_KEY = "API_KEY"


@pytest.fixture(scope="session")
def api_key():
    return "TEST"


@pytest.fixture(scope="session")
def max_retries():
    return 3


@pytest.fixture(scope="session")
def stamphq_client(api_key, max_retries):
    return StampHQClient(api_key=api_key, max_retries=max_retries)
