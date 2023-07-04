"""aaa

Revision ID: 6ae069a19709
Revises: 
Create Date: 2023-07-03 01:23:51.993150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ae069a19709'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=999), nullable=True),
    sa.Column('number', sa.String(length=999), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expenses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('money', sa.Numeric(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.String(length=999), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('incomes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('money', sa.Numeric(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.String(length=999), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=999), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('amount_type', sa.String(length=999), nullable=True),
    sa.Column('category', sa.String(length=999), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trades',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=999), nullable=True),
    sa.Column('password', sa.String(length=999), nullable=True),
    sa.Column('password_hash', sa.String(length=999), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('trades')
    op.drop_table('products')
    op.drop_table('orders')
    op.drop_table('incomes')
    op.drop_table('expenses')
    op.drop_table('customers')
    # ### end Alembic commands ###
