"""Interfaces for object which have string representation."""
from typing import Protocol


class Stringable(Protocol):
    """Sync stringable objects interface."""

    def __str__(self):
        """Representation.

        :raises NotImplementedError: if not implemented
        """
        raise NotImplementedError


class AsyncStringable(Protocol):
    """Async stringable objects interface."""

    async def to_str(self):
        """Representation.

        :raises NotImplementedError: if not implemented
        """
        raise NotImplementedError
