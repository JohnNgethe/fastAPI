"""Create Post Table

Revision ID: 83e9bb7482bf
Revises: 
Create Date: 2023-03-07 20:29:34.481344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83e9bb7482bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
