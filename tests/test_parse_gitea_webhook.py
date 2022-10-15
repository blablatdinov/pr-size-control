import pytest

import json

from pr_size_control.gitea_pr_num import GiteaPRIndex


@pytest.fixture
def webhook_json():
    with open('tests/fixtures/gitea_webhook_example.json', 'r') as file:
        return json.loads(file.read())


async def test(webhook_json):
    got = await GiteaPRIndex(webhook_json).value()

    assert got == 1
