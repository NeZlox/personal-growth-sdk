from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from personal_growth_sdk.authorization.models.enums.role import RoleType

from .session_response_schema import SessionResponseTemplate
from .user_response_schema import UserResponseTemplate

__all__ = ['UserCreateRequest', 'UserLoginRequest', 'UserResponse', 'UserUpdateRequest']


class UserCreateRequest(Struct, forbid_unknown_fields=True):
    """
    Request schema for creating a new user.
    """

    email: Annotated[
        str,
        Parameter(title='Email', description='The user email address.')
    ]

    password: Annotated[
        str,
        Parameter(title='Password', description='The user password.')
    ]
    role: Annotated[
        RoleType,
        Parameter(title='User Role', description='The system role of the user, defining access level.')
    ]


class UserUpdateRequest(Struct, forbid_unknown_fields=True):
    """
    Request schema for updating an existing user.
    """

    email: Annotated[
        str | None,
        Parameter(title='Email', description='The user email address.')
    ] = None

    password: Annotated[
        str | None,
        Parameter(title='Password', description='The user password.')
    ] = None

    role: Annotated[
        RoleType,
        Parameter(title='User Role', description='Системная роль пользователя, определяющая уровень доступа')
    ] = None


class UserResponse(UserResponseTemplate):
    """
    Response schema containing user information and active sessions.
    """

    active_sessions: Annotated[
        list[SessionResponseTemplate],
        Parameter(
            description=(
                'List of active refresh sessions associated with the user. '
                'This is considered a private field and is only included in responses '
                'for endpoints accessible to users with the DEVELOPER role.'
            )
        )
    ] = None


class UserLoginRequest(Struct, forbid_unknown_fields=True):
    """
    Request schema for user login containing authentication credentials.
    """
    email: Annotated[
        str,
        Parameter(title='Email', description='The user email address.')
    ]
    password: Annotated[
        str,
        Parameter(title='Password', description='The user password.')
    ]
