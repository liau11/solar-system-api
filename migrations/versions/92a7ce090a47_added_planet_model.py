"""added planet model

Revision ID: 92a7ce090a47
Revises: 
Create Date: 2023-05-01 19:01:46.025299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "92a7ce090a47"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "planet",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=80), nullable=True),
        sa.Column("description", sa.String(length=200), nullable=True),
        sa.Column("is_planet", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "solar_system",
        sa.Column("id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("name", sa.VARCHAR(length=70), autoincrement=False, nullable=True),
        sa.Column("description", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("is_planet", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="solar_system_pkey"),
    )
    op.drop_table("planet")
    # ### end Alembic commands ###
