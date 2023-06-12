import pytest
from client import get_index_price


# Mock response for testing
class MockResponse:
    def __init__(self, text, status):
        self._text = text
        self.status = status

    async def text(self):
        return self._text

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return self


@pytest.mark.asyncio
async def test_get_index_price(mocker):
    text = "{\"result\": {\"index_price\": 25000}}"
    status = 200
    mocker.patch('aiohttp.ClientSession.get', return_value=MockResponse(text=text, status=status))

    result = await get_index_price('btc')
    assert result == 25000
