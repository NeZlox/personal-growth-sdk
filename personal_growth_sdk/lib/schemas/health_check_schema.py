import enum
from typing import Any

import msgspec

__all__ = [
    'DependencyHealth',
    'DependencyType',
    'HealthSchema',
    'HealthStatus'
]


class HealthStatus(enum.StrEnum):
    """
    Enum representing possible health statuses.
    """

    OK = enum.auto()
    ERROR = enum.auto()


class DependencyType(enum.StrEnum):
    """
    Enum representing types of dependencies.
    """

    REDIS = 'redis'
    POSTGRES = 'postgres'
    RABBITMQ = 'rabbitmq'
    HTTP = 'http'


class DependencyHealth(msgspec.Struct):
    """
    Struct representing health status of a dependency.
    """

    type: DependencyType
    name: str | None
    status: HealthStatus
    details: dict[str, Any] | None


class HealthSchema(msgspec.Struct):
    """
    Struct representing overall health status.
    """

    status: HealthStatus
    deps: list[DependencyHealth]
