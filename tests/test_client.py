import pytest

from stamphq.client import StampHQClient, ERR_API_KEY_NEEDED


class TestStampHQClient:
    def test_client_init(self, stamphq_client):
        assert stamphq_client is not None
        assert stamphq_client._api_key is not None
        assert stamphq_client.max_retries == 3

    def test_no_token(self):
        with pytest.raises(AssertionError) as exc:
            StampHQClient(api_key="")
        assert str(exc.value).startswith(ERR_API_KEY_NEEDED)

    def test_repr(self, stamphq_client, api_key, max_retries):
        assert repr(stamphq_client) == f"<StampHQClient: {api_key}, max_retries={max_retries}>"
