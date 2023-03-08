"""auto vote tables

Revision ID: 40c90c4b93b5
Revises: 5d73c5ebca4b
Create Date: 2023-03-08 15:32:03.503114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40c90c4b93b5'
down_revision = '5d73c5ebca4b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###
