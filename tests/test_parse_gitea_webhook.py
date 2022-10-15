"""Test parse gitea webhook."""
import pytest
from jinja2 import Template

from pr_size_control.gitea_pr_num import GiteaPRIndex


def _render_webhook_json(pr_id: int):
    with open('tests/fixtures/gitea_webhook_example.json', 'r') as webhook:
        return Template(webhook.read()).render(pr_id=pr_id)


@pytest.fixture
def webhook_json():
    """Webhook json fixture."""
    return _render_webhook_json


@pytest.mark.parametrize('pr_id', [1, 44, 98])
def test(webhook_json, pr_id):
    """Test parse pull request index."""
    got = int(GiteaPRIndex(webhook_json(pr_id)))

    assert got == pr_id
