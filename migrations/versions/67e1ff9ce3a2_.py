"""empty message

Revision ID: 67e1ff9ce3a2
Revises: 6665010002ad
Create Date: 2024-10-07 20:46:15.865052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67e1ff9ce3a2'
down_revision = '6665010002ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=16), nullable=True),
    sa.Column('stop_loss_pct', sa.Float(), nullable=True),
    sa.Column('trailing_stop_pct', sa.Float(), nullable=True),
    sa.Column('take_profit_pct', sa.Float(), nullable=True),
    sa.Column('lookback_days', sa.String(length=16), nullable=True),
    sa.Column('bot_running', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=56), nullable=False),
    sa.Column('name', sa.String(length=56), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('last_login', sa.DateTime(), nullable=False),
    sa.Column('control_panel_access', sa.Boolean(), nullable=False),
    sa.Column('admin_panel_access', sa.Boolean(), nullable=False),
    sa.Column('email_raports_receiver', sa.Boolean(), nullable=False),
    sa.Column('login_errors', sa.Integer(), nullable=False),
    sa.Column('account_suspended', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('settings')
    # ### end Alembic commands ###
