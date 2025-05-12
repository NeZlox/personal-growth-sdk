from __future__ import annotations

from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from personal_growth_sdk.multi_agent.models.enums import ChatRole

from .chat_template_schema import ChatResponse
from .message_template_schema import MessageResponse

__all__ = [
    'MessageCreateRequest',
    'MessageDetailResponse',
    'MessageResponse',
    'MessageUpdateRequest'
]


class MessageCreateRequest(Struct, forbid_unknown_fields=True):
    """
    Request schema for creating a new chat message.
    """

    chat_id: Annotated[
        int,
        Parameter(description='ID of the chat to which the message will be added.')
    ]

    role: Annotated[
        ChatRole,
        Parameter(description='Role of the message sender.')
    ]

    content: Annotated[
        str,
        Parameter(description='Text content of the message to be created.')
    ]


class MessageUpdateRequest(Struct, forbid_unknown_fields=True):
    """
    Request schema for updating the content of an existing message.
    """

    content: Annotated[
        str,
        Parameter(description='Updated text content of the message.')
    ]


class MessageDetailResponse(MessageResponse):
    """
    Extended message response that includes a reference to the parent chat.
    """

    chat: Annotated[
        ChatResponse | None,
        Parameter(description='Embedded chat summary. Usually excluded from list responses.')
    ] = None
