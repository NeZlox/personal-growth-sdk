from __future__ import annotations

import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

__all__ = ['CategoryResponse']


class CategoryResponse(Struct, forbid_unknown_fields=True, kw_only=True):
    """
    Response schema representing a category object.
    """

    id: Annotated[
        int,
        Parameter(description='Category identifier'),
    ]
    name: Annotated[
        str,
        Parameter(description='Display name of the category'),
    ]

    userId: Annotated[  # noqa: N815
        int | None,
        Parameter(description='Owner user ID (`null` for system-level categories)'),
    ] = None

    color: Annotated[
        str | None,
        Parameter(description='Hex colour or *null*'),
    ] = None

    description: Annotated[
        str | None,
        Parameter(description='Free-form description'),
    ] = None

    parentId: Annotated[  # noqa: N815
        int | None,
        Parameter(description='Parent category ID for nested hierarchies'),
    ] = None

    isSystem: Annotated[  # noqa: N815
        bool,
        Parameter(description='`true`→ predefined, non-removable category'),
    ] = False

    createdAt: Annotated[  # noqa: N815
        datetime.datetime,
        Parameter(description='Creation timestamp (RFC 3339)'),
    ]

    updatedAt: Annotated[  # noqa: N815
        datetime.datetime,
        Parameter(description='Last modification timestamp (RFC 3339)'),
    ]
