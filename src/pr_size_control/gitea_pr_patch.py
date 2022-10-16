import httpx
from pr_size_control.exceptions.gitea_exceptions import GiteaException

from pr_size_control.stringabe import AsyncStringable


class GiteaPRPatch(AsyncStringable):

    def __init__(self, link_to_patch: str):
        self._link_to_patch = link_to_patch

    async def to_str(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(self._link_to_patch)
            if response.status_code != 200:
                raise GiteaException(
                    "Can't get patch file. Status {0}".format(response.status),
                )
            return response.text
