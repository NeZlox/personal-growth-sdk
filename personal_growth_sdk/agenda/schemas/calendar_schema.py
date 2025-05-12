from __future__ import annotations

import datetime
from enum import StrEnum
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

__all__ = ['CalendarCreateRequest', 'CalendarPatchRequest', 'CalendarResponse']


class Visibility(StrEnum):
    """
    Calendar visibility level for other users.
    """

    PRIVATE = 'private'
    PUBLIC = 'public'
    CONFIDENTIAL = 'confidential'


class TimezoneInfo(Struct, forbid_unknown_fields=True):
    """
    Read-only timezone object included in CalendarResponse.

    Only `id`, `name`, and `tzdata` are guaranteed by the API spec. Timestamps are optional.
    """

    id: Annotated[
        int,
        Parameter(description='Internal identifier of the timezone record.'),
    ]

    name: Annotated[
        str,
        Parameter(description='IANA time-zone identifier, e.g. *Europe/Berlin*.'),
    ]

    tzdata: Annotated[
        str,
        Parameter(description='tzdata / ICU zone name used by the service.'),
    ]

    lastUpdated: Annotated[  # noqa: N815
        datetime.datetime | None,
        Parameter(description='When tzdata for this zone was refreshed (RFC 3339).'),
    ] = None

    createdAt: Annotated[  # noqa: N815
        datetime.datetime | None,
        Parameter(description='Timestamp when this timezone entry was created.'),
    ] = None

    updatedAt: Annotated[  # noqa: N815
        datetime.datetime | None,
        Parameter(description='Last modification timestamp of the timezone entry.'),
    ] = None


class TimezonePayload(Struct, forbid_unknown_fields=True):
    """
    Writable timezone object for use in create/patch requests.

    Matches the TimezoneInfo structure but is client-supplied.
    """

    id: Annotated[
        int,
        Parameter(description='Existing timezone id returned earlier by the service.'),
    ]

    name: Annotated[
        str,
        Parameter(description='IANA time-zone identifier.'),
    ]

    tzdata: Annotated[
        str,
        Parameter(description='tzdata / ICU zone name.'),
    ]

    lastUpdated: Annotated[  # noqa: N815
        datetime.datetime | None,
        Parameter(description='When tzdata was refreshed (RFC 3339).'),
    ] = None

    createdAt: Annotated[  # noqa: N815
        datetime.datetime | None,
        Parameter(description='Entry creation moment (RFC 3339).'),
    ] = None

    updatedAt: Annotated[  # noqa: N815
        datetime.datetime | None,
        Parameter(description='Last update moment (RFC 3339).'),
    ] = None


class CalendarResponse(Struct, forbid_unknown_fields=True, kw_only=True):
    """
    Response schema representing a calendar object.
    """

    id: Annotated[
        int,
        Parameter(description='Calendar record identifier'),
    ]

    userId: Annotated[  # noqa: N815
        int,
        Parameter(description='Owner user identifier (external system)'),
    ]

    name: Annotated[
        str,
        Parameter(description='Calendar display name'),
    ]

    description: Annotated[
        str | None,
        Parameter(description='Optional calendar description'),
    ] = None

    color: Annotated[
        str | None,
        Parameter(description='Optional colour (hex or named value)'),
    ] = None

    isPrimary: Annotated[  # noqa: N815
        bool,
        Parameter(description='`true` → default calendar for the user'),
    ] = False

    visibility: Annotated[
        Visibility,
        Parameter(description='Access level for other users'),
    ]

    timezone: Annotated[
        TimezoneInfo | None,
        Parameter(description='Timezone metadata or *null*'),
    ] = None


class CalendarCreateRequest(Struct, forbid_unknown_fields=True, kw_only=True):
    """
    Request body for creating a new calendar.
    """

    id: Annotated[
        int,
        Parameter(description='Client-supplied calendar identifier'),
    ]

    userId: Annotated[  # noqa: N815
        int,
        Parameter(description='Owner user identifier'),
    ]

    name: Annotated[
        str,
        Parameter(description='Calendar display name'),
    ]

    description: Annotated[
        str | None,
        Parameter(description='Optional calendar description'),
    ] = None

    color: Annotated[
        str | None,
        Parameter(description='Optional colour (hex or named value)'),
    ] = None

    isPrimary: Annotated[  # noqa: N815
        bool,
        Parameter(description='`true` → default calendar for the user'),
    ] = False

    visibility: Annotated[
        Visibility,
        Parameter(description='Access level for other users'),
    ]

    timezone: Annotated[
        TimezonePayload | None,
        Parameter(description='Existing timezone to link or *null*'),
    ] = None


class CalendarPatchRequest(Struct, forbid_unknown_fields=True):
    """
    Request body for partially updating a calendar.
    """

    id: Annotated[
        int,
        Parameter(description='Target calendar identifier'),
    ]

    userId: Annotated[  # noqa: N815
        int,
        Parameter(description='Owner user identifier'),
    ]

    name: Annotated[
        str,
        Parameter(description='Calendar display name'),
    ]

    description: Annotated[
        str | None,
        Parameter(description='Calendar description (nullable)'),
    ] = None

    color: Annotated[
        str | None,
        Parameter(description='Colour (nullable)'),
    ] = None

    isPrimary: Annotated[  # noqa: N815
        bool | None,
        Parameter(description='Marks this calendar as user`s primary'),
    ] = None

    visibility: Annotated[
        Visibility | None,
        Parameter(description='Visibility change'),
    ] = None

    timezone: Annotated[
        TimezonePayload | None,
        Parameter(description='Replace linked timezone or set *null*'),
    ] = None
