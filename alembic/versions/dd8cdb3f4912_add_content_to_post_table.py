"""add content to post table

Revision ID: dd8cdb3f4912
Revises: 83e9bb7482bf
Create Date: 2023-03-08 12:21:17.213725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd8cdb3f4912'
down_revision = '83e9bb7482bf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts',
                   'content')
    pass
