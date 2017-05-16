from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['character'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['character'].drop()
