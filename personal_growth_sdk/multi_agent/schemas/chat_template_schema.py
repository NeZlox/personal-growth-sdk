"""
Lightweight representation of a chat.

Used as a base class for detailed responses and embedded inside other schemas
(e.g., MessageDetailResponse) to prevent circular references.
"""

from __future__ import annotations

import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

__all__ = ['ChatResponse']


class ChatResponse(Struct, forbid_unknown_fields=True):
    """
    Minimal representation of a chat session.
    """

    id: Annotated[
        int,
        Parameter(description='Unique identifier of the chat session.')
    ]

    user_id: Annotated[
        int,
        Parameter(description='External user identifier (not a foreign key).')
    ]

    created_at: Annotated[
        datetime.datetime,
        Parameter(description='Timestamp of when the chat was created (ISO 8601 format).')
    ]

    updated_at: Annotated[
        datetime.datetime,
        Parameter(description='Timestamp of the last update to the chat (ISO 8601 format).')
    ]
