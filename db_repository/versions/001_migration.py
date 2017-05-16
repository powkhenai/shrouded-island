from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
character = Table('character', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('firstName', VARCHAR(length=250)),
    Column('lastName', VARCHAR(length=250)),
    Column('height', INTEGER),
    Column('weight', INTEGER),
    Column('age', INTEGER),
    Column('hp', INTEGER),
    Column('exp', INTEGER),
    Column('iq', INTEGER),
    Column('me', INTEGER),
    Column('ma', INTEGER),
    Column('ps', INTEGER),
    Column('pp', INTEGER),
    Column('pe', INTEGER),
    Column('pb', INTEGER),
    Column('spd', INTEGER),
    Column('user_id', INTEGER),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=250), nullable=False),
    Column('password', VARCHAR(length=250), nullable=False),
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
    pre_meta.tables['character'].drop()
    pre_meta.tables['user'].columns['password'].drop()
    pre_meta.tables['user'].columns['username'].drop()
    post_meta.tables['user'].columns['login_token'].create()
    post_meta.tables['user'].columns['name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['character'].create()
    pre_meta.tables['user'].columns['password'].create()
    pre_meta.tables['user'].columns['username'].create()
    post_meta.tables['user'].columns['login_token'].drop()
    post_meta.tables['user'].columns['name'].drop()
