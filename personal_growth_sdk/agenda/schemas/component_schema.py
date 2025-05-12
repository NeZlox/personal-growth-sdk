import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

__all__ = ['ComponentCreateRequest', 'ComponentPatchRequest', 'ComponentResponse']


class ComponentResponse(Struct, forbid_unknown_fields=True, kw_only=True):
    """
    Response schema representing a component object.
    """

    id: Annotated[
        int,
        Parameter(description='Unique component identifier'),
    ]

    calendarId: Annotated[  # noqa: N815
        int,
        Parameter(description='ID of the calendar to which this component belongs.'),
    ]

    summary: Annotated[
        str,
        Parameter(description='Short title or summary of the component.'),
    ]

    componentType: Annotated[  # noqa: N815
        str,
        Parameter(description='Type of component.'),
    ]

    description: Annotated[
        str | None,
        Parameter(description='Full description'),
    ] = None

    dtstart: Annotated[
        datetime.datetime,
        Parameter(description='Start date and time of the component (RFC 3339).'),
    ]

    dtend: Annotated[
        datetime.datetime,
        Parameter(description='End date and time of the component (RFC 3339).'),
    ]

    isRecurring: Annotated[  # noqa: N815
        bool,
        Parameter(description='True if this component repeats in time.'),
    ] = False

    recurrenceId: Annotated[  # noqa: N815
        int | None,
        Parameter(description='ID of the recurring parent component (if any).'),
    ] = None

    status: Annotated[
        str,
        Parameter(description='Current status of the component (e.g., confirmed, cancelled).'),
    ]

    priority: Annotated[
        int,
        Parameter(description='Component priority (lower = more important).'),
    ]
    hasDependencies: Annotated[  # noqa: N815
        bool,
        Parameter(description='True if this component depends on others.'),
    ] = False
    hasDependentTasks: Annotated[  # noqa: N815
        bool,
        Parameter(description='True if other tasks depend on this component.'),
    ] = False

    createdAt: Annotated[  # noqa: N815
        datetime.datetime,
        Parameter(description='Creation timestamp (RFC 3339).'),
    ]

    updatedAt: Annotated[  # noqa: N815
        datetime.datetime,
        Parameter(description='Last updated timestamp (RFC 3339).'),
    ]


class ComponentCreateRequest(Struct, forbid_unknown_fields=True):
    """
    Request schema for creating a new component.
    """
    pass


class ComponentPatchRequest(Struct, forbid_unknown_fields=True):
    """
    Request schema for partially updating a component.
    """
    pass
