"""lottery table

Revision ID: 4e02f645551a
Revises: 124a8d5f7051
Create Date: 2021-11-26 11:28:11.596275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e02f645551a'
down_revision = '124a8d5f7051'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Lottery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lottery_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('User')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('lottery_number', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Lottery')
    # ### end Alembic commands ###