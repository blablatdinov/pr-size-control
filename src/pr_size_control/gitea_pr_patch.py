"""Module contain class for working with gitea pull request patch."""
from http import HTTPStatus

import httpx

from pr_size_control.exceptions.gitea_exceptions import GiteaBaseError
from pr_size_control.stringabe import AsyncStringable


class GiteaPRPatch(AsyncStringable):
    """Gitea pull request patch."""

    def __init__(self, link_to_patch: str):
        """Class constructor.

        :param link_to_patch: str
        """
        self._link_to_patch = link_to_patch

    async def to_str(self):
        """Representation.

        :return: str
        :raises GiteaBaseError: if app can't get pull request patch
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(self._link_to_patch)
            if response.status_code != HTTPStatus.OK:
                raise GiteaBaseError(
                    "Can't get patch file. Status {0}".format(response.status),
                )
            return response.text
