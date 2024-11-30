"""слияние голов

Revision ID: f709cf6daa49
Revises: 2f008ba8589a, e3fb4e9f355e
Create Date: 2024-11-30 18:30:33.538272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f709cf6daa49'
down_revision: Union[str, None] = ('2f008ba8589a', 'e3fb4e9f355e') # type: ignore
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('users','Full_name')


def downgrade() -> None:
    op.add_column('users', sa.Column('Full_name', sa.String(), nullable=False))
