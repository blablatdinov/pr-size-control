"""Module with class for find pr index."""
import json

from pr_size_control.intable import Intable


class GiteaPRIndex(Intable):
    """Gitea pull request index."""

    def __init__(self, webhook_json: str):
        """Class constructor.

        :param webhook_json: str
        """
        self._webhook_json = webhook_json

    def __int__(self):
        """Integer representation.

        :return: int
        """
        return json.loads(self._webhook_json)['pull_request']['number']
