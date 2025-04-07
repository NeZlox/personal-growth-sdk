from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import Enum, Index, String, UniqueConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from personal_growth_sdk.authorization.models.base import authorization_metadata

from .enums import RoleType

if TYPE_CHECKING:
    from .session import Session

__all__ = ['User']


class User(BigIntAuditBase):
    """
    Model representing a system user.
    """
    metadata = authorization_metadata

    @declared_attr.directive
    @classmethod
    def __table_args__(cls):
        return (
            Index('idx_user_email', 'email'),
            UniqueConstraint('email', name='uq_user_email'),
            {'comment': 'Table of system users.'}
        )

    email: Mapped[str] = mapped_column(
        String(255),
        comment='User email address.'
    )
    password: Mapped[str] = mapped_column(
        String(255),
        comment='User password (encrypted or hashed).'
    )
    role: Mapped[RoleType] = mapped_column(
        Enum(RoleType, native_enum=False, length=50),
        comment='User role in the system.'
    )

    active_sessions: Mapped[list['Session']] = relationship(
        'Session',
        back_populates='user',
        uselist=True,
        cascade='all, delete-orphan'
    )
