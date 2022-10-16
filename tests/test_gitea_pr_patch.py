"""Testing GiteaPRPatch class."""
from pathlib import Path

import pytest
import respx
from httpx import Response

from pr_size_control.gitea_pr_patch import GiteaPRPatch


@pytest.fixture()
def patch_fixture():
    """Patch fixture for mocking http request."""
    return Path('tests/fixtures/git_patch_example.patch').read_text()


@respx.mock
async def test(patch_fixture):
    """Test getting pull request patch."""
    respx.get('https://foo.bar/').mock(return_value=Response(200, text=patch_fixture))
    got = await GiteaPRPatch('https://foo.bar/').to_str()

    assert got == patch_fixture
