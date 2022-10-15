# TODO: create interface
class GiteaPRPatch(object):

    def __init__(self, pr_idx):
        self._pr_idx = pr_idx

    async def value(self):
        return 'lol'
