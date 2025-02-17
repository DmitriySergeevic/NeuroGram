"""rename field req_limit

Revision ID: 1d114758e584
Revises: 6eb975c04e89
Create Date: 2024-12-21 03:22:54.515434

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1d114758e584"
down_revision: Union[str, None] = "6eb975c04e89"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("subscription", sa.Column("req_limit", sa.Integer(), nullable=False))
    op.drop_column("subscription", "total_req")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "subscription",
        sa.Column("total_req", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_column("subscription", "req_limit")
    # ### end Alembic commands ###
