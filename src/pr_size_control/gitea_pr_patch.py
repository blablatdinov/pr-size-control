# TODO: create interface
class GiteaPRPatch(object):

    def __init__(self, link_to_patch: str):
        self._link_to_patch = link_to_patch

    async def value(self):
        return 'lol'
