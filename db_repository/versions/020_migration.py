from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
character = Table('character', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=150)),
    Column('last_name', String(length=150)),
    Column('race', String(length=150)),
    Column('occ', String(length=150)),
    Column('sex', String(length=1)),
    Column('height', Integer),
    Column('weight', Integer),
    Column('age', Integer),
    Column('hp', Integer),
    Column('sdc', Integer),
    Column('exp', Integer),
    Column('lvl', Integer),
    Column('iq', Integer),
    Column('me', Integer),
    Column('ma', Integer),
    Column('ps', Integer),
    Column('pp', Integer),
    Column('pe', Integer),
    Column('pb', Integer),
    Column('spd', Integer),
    Column('sav_sm', Integer),
    Column('sav_rm', Integer),
    Column('sav_psi', Integer),
    Column('sav_tp', Integer),
    Column('sav_hd', Integer),
    Column('sav_in', Integer),
    Column('sav_pos', Integer),
    Column('sav_hf', Integer),
    Column('sav_cd', Integer),
    Column('sav_pn', Integer),
    Column('alignment', Integer),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['character'].columns['sav_cd'].create()
    post_meta.tables['character'].columns['sav_hd'].create()
    post_meta.tables['character'].columns['sav_hf'].create()
    post_meta.tables['character'].columns['sav_in'].create()
    post_meta.tables['character'].columns['sav_pn'].create()
    post_meta.tables['character'].columns['sav_pos'].create()
    post_meta.tables['character'].columns['sav_psi'].create()
    post_meta.tables['character'].columns['sav_rm'].create()
    post_meta.tables['character'].columns['sav_sm'].create()
    post_meta.tables['character'].columns['sav_tp'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['character'].columns['sav_cd'].drop()
    post_meta.tables['character'].columns['sav_hd'].drop()
    post_meta.tables['character'].columns['sav_hf'].drop()
    post_meta.tables['character'].columns['sav_in'].drop()
    post_meta.tables['character'].columns['sav_pn'].drop()
    post_meta.tables['character'].columns['sav_pos'].drop()
    post_meta.tables['character'].columns['sav_psi'].drop()
    post_meta.tables['character'].columns['sav_rm'].drop()
    post_meta.tables['character'].columns['sav_sm'].drop()
    post_meta.tables['character'].columns['sav_tp'].drop()
