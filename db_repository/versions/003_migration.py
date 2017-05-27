from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
char_skills = Table('char_skills', post_meta,
    Column('char_id', Integer),
    Column('skill_id', Integer),
)

skill = Table('skill', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=150)),
    Column('description', String),
    Column('category', String(length=50)),
    Column('base', Integer),
    Column('per_level', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['char_skills'].create()
    post_meta.tables['skill'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['char_skills'].drop()
    post_meta.tables['skill'].drop()
