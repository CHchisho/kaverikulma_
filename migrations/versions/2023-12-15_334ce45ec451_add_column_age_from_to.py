"""Add column age from to

Revision ID: 334ce45ec451
Revises: 6bddfe038995
Create Date: 2023-12-15 14:42:45.287977

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '334ce45ec451'
down_revision: Union[str, None] = '5b3ab839d984'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('friend_age_from', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('friend_age_to', sa.Integer(), nullable=False))
    op.drop_column('user', 'friend_age')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('friend_age', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('user', 'friend_age_to')
    op.drop_column('user', 'friend_age_from')
    # ### end Alembic commands ###
