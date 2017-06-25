from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
skill = Table('skill', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=150)),
    Column('description', String),
    Column('note', String),
    Column('skill_category', Integer),
    Column('base', Integer),
    Column('per_level', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['skill'].columns['name'].alter(nullable=False, unique=True)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['skill'].columns['name'].alter(type=String(150))
