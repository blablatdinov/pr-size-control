from pr_size_control.intable import Intable


class GiteaPRIndex(Intable):

    def __init__(self, webhook_json: str):
        self._webhook_json = webhook_json

    async def value(self):
        return 1
