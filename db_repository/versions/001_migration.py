from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
char_skills = Table('char_skills', post_meta,
    Column('char_id', Integer, primary_key=True, nullable=False),
    Column('skill_id', Integer, primary_key=True, nullable=False),
    Column('skill_type', String(length=3)),
)

character = Table('character', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=150)),
    Column('last_name', String(length=150)),
    Column('height', Integer),
    Column('weight', Integer),
    Column('age', Integer),
    Column('hp', Integer),
    Column('exp', Integer),
    Column('iq', Integer),
    Column('me', Integer),
    Column('ma', Integer),
    Column('ps', Integer),
    Column('pp', Integer),
    Column('pe', Integer),
    Column('pb', Integer),
    Column('spd', Integer),
    Column('user_id', Integer),
)

skill = Table('skill', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=150)),
    Column('description', String),
    Column('note', String),
    Column('skill_category', Integer),
    Column('base', Integer),
    Column('per_level', Integer),
)

skill_category = Table('skill_category', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=50)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=255)),
    Column('login_token', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['char_skills'].create()
    post_meta.tables['character'].create()
    post_meta.tables['skill'].create()
    post_meta.tables['skill_category'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['char_skills'].drop()
    post_meta.tables['character'].drop()
    post_meta.tables['skill'].drop()
    post_meta.tables['skill_category'].drop()
    post_meta.tables['user'].drop()
