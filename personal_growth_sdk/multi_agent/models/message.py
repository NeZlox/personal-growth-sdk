from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from personal_growth_sdk.multi_agent.models.base import multi_aget_metadata

from .enums import ChatRole

if TYPE_CHECKING:
    from .chat import Chat

__all__ = ['Message']


class Message(BigIntAuditBase):
    """
    Model representing a single chat message (either user input or assistant response).
    """

    metadata = multi_aget_metadata

    @declared_attr.directive
    @classmethod
    def __table_args__(cls):
        return (
            Index('idx_message_chat_id', 'chat_id'),
            {'comment': 'Table storing individual chat messages within a chat session.'}
        )

    chat_id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey('chat.id', ondelete='CASCADE'),
        comment='Foreign key referencing the parent chat session.'
    )

    role: Mapped[ChatRole] = mapped_column(
        String(16),
        nullable=False,
        comment='Role of the message author.'
    )

    content: Mapped[str] = mapped_column(
        Text,
        comment='Text content of the message.'
    )

    chat: Mapped[Chat] = relationship(
        back_populates='messages',
        uselist=False,
        foreign_keys=[chat_id]
    )
