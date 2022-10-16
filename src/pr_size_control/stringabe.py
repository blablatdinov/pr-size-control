from typing import Protocol


class Stringable(Protocol):

    def __str__(self):
        raise NotImplementedError


class AsyncStringable(Protocol):

    async def to_str(self):
        raise NotImplementedError
