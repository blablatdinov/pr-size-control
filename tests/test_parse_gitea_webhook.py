"""Test parse gitea webhook."""
import json

import pytest

from pr_size_control.gitea_pr_num import GiteaPRIndex


@pytest.fixture
def webhook_json():
    """Webhook json fixture."""
    with open('tests/fixtures/gitea_webhook_example.json', 'r') as webhook:
        return json.loads(webhook.read())


def test(webhook_json):
    """Test parse pull request index."""
    got = int(GiteaPRIndex(webhook_json))

    assert got == 1
