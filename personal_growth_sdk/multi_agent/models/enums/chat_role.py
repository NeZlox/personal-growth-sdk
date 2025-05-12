"""
Enum-helpers for chat module.
"""

from enum import StrEnum

__all__ = ['ChatRole']


class ChatRole(StrEnum):
    """
    Author of a chat message.
    """

    USER = 'user'
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
