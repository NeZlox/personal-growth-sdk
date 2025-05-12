"""
This file serves as a bridge for handling relations in responses to avoid circular import dependencies.
"""

import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

__all__ = ['SessionResponseTemplate']


class SessionResponseTemplate(Struct, forbid_unknown_fields=True):
    """
    Response schema for a refresh session.
    """

    id: Annotated[
        int,
        Parameter(description='Unique identifier of the session.')
    ]

    user_id: Annotated[
        int,
        Parameter(description='ID of the user associated with the session.')
    ]

    refresh_token: Annotated[
        str,
        Parameter(description='Hashed refresh token used for authentication.')
    ]

    fingerprint: Annotated[
        str,
        Parameter(description='Browser fingerprint for identifying the client.')
    ]

    user_agent: Annotated[
        str,
        Parameter(description='User agent string of the browser.')
    ]

    ip: Annotated[
        str,
        Parameter(description='IP address of the user.')
    ]

    expires_at: Annotated[
        datetime.datetime,
        Parameter(description='Timestamp indicating when the refresh token expires (ISO 8601 format).')
    ]

    created_at: Annotated[
        datetime.datetime,
        Parameter(description='Timestamp of when the session was created (ISO 8601 format).')
    ]

    updated_at: Annotated[
        datetime.datetime,
        Parameter(description='Timestamp of the last update to the session (ISO 8601 format).')
    ]
