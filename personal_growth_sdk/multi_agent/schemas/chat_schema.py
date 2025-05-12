from __future__ import annotations

from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from .chat_template_schema import ChatResponse
from .message_template_schema import MessageResponse

__all__ = [
    'ChatCreateRequest',
    'ChatDetailResponse',
    'ChatResponse',
    'ChatUpdateRequest'
]


class ChatCreateRequest(Struct, forbid_unknown_fields=True):
    """
    Request schema for creating a new chat.
    """

    user_id: Annotated[
        int,
        Parameter(description='External user identifier.')
    ]


class ChatUpdateRequest(Struct, forbid_unknown_fields=True):
    """
    Request schema for updating chat metadata.
    """
    pass


class ChatDetailResponse(ChatResponse, forbid_unknown_fields=True):
    """
    Detailed response containing full message history.
    """

    messages: Annotated[
        list[MessageResponse] | None,
        Parameter(description='Chronologically ordered list of messages in the chat.')
    ] = None
