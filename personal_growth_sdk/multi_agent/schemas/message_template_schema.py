"""
Lightweight representation of a message.

Used as a base class for detailed responses and embedded inside other schemas
(e.g., ChatDetailResponse) to prevent circular references.
"""

from __future__ import annotations

import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from personal_growth_sdk.multi_agent.models.enums import ChatRole

__all__ = ['MessageResponse']


class MessageResponse(Struct, forbid_unknown_fields=True):
    """
    Minimal representation of a chat message.
    """

    id: Annotated[
        int,
        Parameter(description='Unique identifier of the message.')
    ]

    chat_id: Annotated[
        int,
        Parameter(description='ID of the chat to which this message belongs.')
    ]

    role: Annotated[
        ChatRole,
        Parameter(description='Role of the message sender.')
    ]

    content: Annotated[
        str,
        Parameter(description='Raw text content of the message.')
    ]

    created_at: Annotated[
        datetime.datetime,
        Parameter(description='Timestamp of when the message was created (ISO 8601 format).')
    ]

    updated_at: Annotated[
        datetime.datetime,
        Parameter(description='Timestamp of the last update to the message (ISO 8601 format).')
    ]
