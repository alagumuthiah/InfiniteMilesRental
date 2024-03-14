"""create bookings table

Revision ID: 2a04b6892a9f
Revises: a2e2751494d0
Create Date: 2024-03-13 21:56:57.845947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a04b6892a9f'
down_revision = 'a2e2751494d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('pickupLocation', sa.String(length=255), nullable=True),
    sa.Column('pickupTime', sa.DateTime(), nullable=True),
    sa.Column('dropLocation', sa.String(length=255), nullable=True),
    sa.Column('dropTime', sa.DateTime(), nullable=True),
    sa.Column('carId', sa.Integer(), nullable=True),
    sa.Column('categoryId', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('Completed', 'Active', 'Inactive', 'Cancelled', name='booking_enum'), nullable=True),
    sa.Column('protected', sa.Boolean(), nullable=True),
    sa.Column('cost', sa.Numeric(scale=2), nullable=True),
    sa.Column('paymentMethod', sa.Enum('Paypal', 'card', 'TBC', name='payment_enum'), nullable=True),
    sa.ForeignKeyConstraint(['carId'], ['cars.id'], ),
    sa.ForeignKeyConstraint(['categoryId'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    # ### end Alembic commands ###