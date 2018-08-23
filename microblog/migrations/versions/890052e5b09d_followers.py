"""followers

Revision ID: 890052e5b09d
Revises: 27e0c566f856
Create Date: 2018-08-22 17:06:28.590691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '890052e5b09d'
down_revision = '27e0c566f856'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
