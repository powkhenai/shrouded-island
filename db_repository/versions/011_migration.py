from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
skill_preqs = Table('skill_preqs', post_meta,
    Column('skill_id', Integer, primary_key=True, nullable=False),
    Column('preq_id', Integer, primary_key=True, nullable=False),
)

char_skills = Table('char_skills', post_meta,
    Column('char_id', Integer, primary_key=True, nullable=False),
    Column('skill_id', Integer, primary_key=True, nullable=False),
    Column('skill_type', String(length=3)),
    Column('class_bonus', Integer),
    Column('inherited', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['skill_preqs'].create()
    post_meta.tables['char_skills'].columns['inherited'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['skill_preqs'].drop()
    post_meta.tables['char_skills'].columns['inherited'].drop()
