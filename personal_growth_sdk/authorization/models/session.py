import datetime
from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from advanced_alchemy.types import DateTimeUTC
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from personal_growth_sdk.authorization.models.base import authorization_metadata

if TYPE_CHECKING:
    from .user import User

__all__ = ['Session']


class Session(BigIntAuditBase):
    """
    Model representing a user's refresh token session.
    """
    metadata = authorization_metadata

    @declared_attr.directive
    @classmethod
    def __table_args__(cls):
        return (
            UniqueConstraint(
                'refresh_token', name='uq_refresh_session_refresh_token'
            ),
            {'comment': 'Table of active user sessions'}
        )

    user_id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey('user.id', ondelete='CASCADE'),
        comment='Foreign key referencing the User table.'
    )
    refresh_token: Mapped[str] = mapped_column(
        String(255),
        comment='Refresh Token (encrypted or hashed).'
    )
    fingerprint: Mapped[str] = mapped_column(
        String(255),
        comment='Browser fingerprint.'
    )
    user_agent: Mapped[str] = mapped_column(
        String(255),
        comment='Users\'s user-agent string.'
    )
    ip: Mapped[str] = mapped_column(
        String(15),
        comment='User\'s IP address.'
    )
    expires_at: Mapped[datetime.datetime] = mapped_column(
        DateTimeUTC(timezone=True),
        comment='Expiration date and time of the refresh token (ISO 8601 format).'
    )

    user: Mapped['User'] = relationship(
        'User',
        back_populates='active_sessions',
        uselist=False,
        foreign_keys='Session.user_id',
    )
