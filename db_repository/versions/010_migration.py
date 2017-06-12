from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
char_skills = Table('char_skills', post_meta,
    Column('char_id', Integer, primary_key=True, nullable=False),
    Column('skill_id', Integer, primary_key=True, nullable=False),
    Column('skill_type', String(length=3)),
    Column('class_bonus', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['char_skills'].columns['class_bonus'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['char_skills'].columns['class_bonus'].drop()
