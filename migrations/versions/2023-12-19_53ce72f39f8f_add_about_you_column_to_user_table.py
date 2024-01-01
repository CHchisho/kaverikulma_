"""Add about_you column to user table

Revision ID: 53ce72f39f8f
Revises: e6583d6541d8
Create Date: 2023-12-19 20:55:34.030977

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53ce72f39f8f'
down_revision: Union[str, None] = 'e6583d6541d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_you', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'about_you')
    # ### end Alembic commands ###