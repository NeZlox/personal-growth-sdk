"""
This file serves as a bridge for handling relations in responses to avoid circular import dependencies.
"""

from __future__ import annotations

import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from personal_growth_sdk.authorization.models.enums import RoleType

__all__ = ['UserResponseTemplate']


class UserResponseTemplate(Struct, forbid_unknown_fields=True):
    """
    Response schema for a user.
    """

    id: Annotated[
        int,
        Parameter(description='Unique identifier of the user.')
    ]

    email: Annotated[
        str,
        Parameter(description='Email address of the user.')
    ]

    role: Annotated[
        RoleType,
        Parameter(description='System role assigned to the user.')
    ]

    created_at: Annotated[
        datetime.datetime,
        Parameter(description='Timestamp when the user was created (ISO 8601 format).')
    ]

    updated_at: Annotated[
        datetime.datetime,
        Parameter(description='Timestamp of the last update to the user record (ISO 8601 format).')
    ]
