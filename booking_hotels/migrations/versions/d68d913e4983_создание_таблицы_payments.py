"""Создание Таблицы 'payments'

Revision ID: d68d913e4983
Revises: 73dd8c40a838
Create Date: 2024-12-03 19:34:01.328296

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd68d913e4983'
down_revision: Union[str, None] = '73dd8c40a838'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'payments',
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("status", sa.String, nullable=False,default="in progress"),
            sa.Column("amount", sa.Float, nullable=False),
            sa.Column("currency", sa.String, nullable=False),
            sa.Column("description", sa.String, nullable=False),
            sa.Column("order_id", sa.String, nullable=False),
            sa.Column("invoice_id", sa.String, nullable=False),
            sa.Column("payment_type", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('payments')