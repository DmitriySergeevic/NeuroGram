"""Create table chat, message and create relationship

Revision ID: 48629c54f97a
Revises: 6233bb6c44eb
Create Date: 2024-12-26 21:04:20.993473

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "48629c54f97a"
down_revision: Union[str, None] = "6233bb6c44eb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "chat",
        sa.Column("id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.BIGINT(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_chat_user_id"), "chat", ["user_id"], unique=False)
    op.create_table(
        "message",
        sa.Column("id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("chat_id", sa.BIGINT(), nullable=False),
        sa.Column("text", sa.String(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("is_bot", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["chat_id"],
            ["chat.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_message_chat_id"), "message", ["chat_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_message_chat_id"), table_name="message")
    op.drop_table("message")
    op.drop_index(op.f("ix_chat_user_id"), table_name="chat")
    op.drop_table("chat")
    # ### end Alembic commands ###
