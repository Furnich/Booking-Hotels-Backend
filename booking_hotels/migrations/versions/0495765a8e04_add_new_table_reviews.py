"""add new table 'reviews'

Revision ID: 0495765a8e04
Revises: f709cf6daa49
Create Date: 2024-11-30 20:59:44.017363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0495765a8e04'
down_revision: Union[str, None] = 'f709cf6daa49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'reviews',
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("hotel_id", sa.Integer(), nullable=False),
            sa.Column("user_id", sa.Integer(), sa.ForeignKey('hotels.id'), nullable=False),
            sa.Column("first_name", sa.String(),nullable=False),
            sa.Column("last_name", sa.String(),nullable=False),
            sa.Column("rating_name", sa.Integer(),nullable=False),
            sa.Column("text", sa.String(),nullable=False),
    )


def downgrade() -> None:
    op.drop_table('reviews')

