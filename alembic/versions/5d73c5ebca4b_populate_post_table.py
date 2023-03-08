"""populate post table

Revision ID: 5d73c5ebca4b
Revises: 2c80d9d1db0b
Create Date: 2023-03-08 15:07:39.599178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d73c5ebca4b'
down_revision = '2c80d9d1db0b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
