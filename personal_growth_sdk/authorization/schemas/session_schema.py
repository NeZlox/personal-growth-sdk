from __future__ import annotations

import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from .session_response_schema import SessionResponseTemplate
from .user_response_schema import UserResponseTemplate

__all__ = ['SessionCreateRequest', 'SessionResponse', 'SessionUpdateRequest']


class SessionCreateRequest(Struct, forbid_unknown_fields=True):
    """
    Request schema for creating a refresh session.
    """

    user_id: Annotated[
        int,
        Parameter(title='User ID', description='ID of the user to whom the session belongs.')
    ]

    refresh_token: Annotated[
        str,
        Parameter(title='Refresh Token', description='Hashed refresh token.')
    ]

    fingerprint: Annotated[
        str,
        Parameter(title='Fingerprint', description='Browser fingerprint.')
    ]

    user_agent: Annotated[
        str,
        Parameter(title='User Agent', description='User\'s browser user-agent string.')
    ]

    ip: Annotated[
        str,
        Parameter(title='IP Address', description='Client\'s IP address.')
    ]

    expires_at: Annotated[
        datetime.datetime,
        Parameter(title='Expires At', description='Expiration time of the refresh token (ISO 8601 format).')
    ]


class SessionUpdateRequest(Struct, forbid_unknown_fields=True):
    """
    Request schema for updating a refresh session.
    """

    refresh_token: Annotated[
        str | None,
        Parameter(title='Refresh Token', description='Hashed refresh token.')
    ] = None

    fingerprint: Annotated[
        str | None,
        Parameter(title='Fingerprint', description='Browser fingerprint.')
    ] = None

    user_agent: Annotated[
        str | None,
        Parameter(title='User Agent', description='User\'s browser user-agent string.')
    ] = None

    ip: Annotated[
        str | None,
        Parameter(title='IP Address', description='Client\'s IP address.')
    ] = None

    expires_at: Annotated[
        datetime.datetime | None,
        Parameter(title='Expires At', description='Expiration time of the refresh token (ISO 8601 format).')
    ] = None


class SessionResponse(SessionResponseTemplate):
    """
    Response schema for a refresh session.
    """

    user: Annotated[
        UserResponseTemplate,
        Parameter(
            description=(
                'User associated with the refresh session. '
                'This is considered a private field and is only included in responses '
                'for endpoints accessible to users with the DEVELOPER role.'
            )
        )
    ] = None
