from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from personal_growth_sdk.multi_agent.models.base import multi_aget_metadata

if TYPE_CHECKING:
    from .message import Message

__all__ = ['Chat']


class Chat(BigIntAuditBase):
    """
    Model representing a chat session between an external end-user and the assistant.
    """

    metadata = multi_aget_metadata

    @declared_attr.directive
    @classmethod
    def __table_args__(cls):
        return (

            {'comment': 'Table storing chat sessions between users and the assistant.'}
        )

    user_id: Mapped[int] = mapped_column(
        BIGINT,
        nullable=False,
        comment='Raw external user ID (not a foreign key).'
    )

    messages: Mapped[list[Message]] = relationship(
        back_populates='chat',
        cascade='all, delete-orphan',
        lazy='raise'
    )
