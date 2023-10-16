"""create todos table

Revision ID: 0f79469d2bd3
Revises: 
Create Date: 2023-10-15 21:07:07.588455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0f79469d2bd3"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE todos (
            id bigserial primary key,
            name text,
            completed boolean not null default false
        );
    """
    )


def downgrade() -> None:
    op.execute("DROP TABLE todos;")
