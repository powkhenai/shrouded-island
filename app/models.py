from sqlalchemy.ext.hybrid import hybrid_property
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    login_token = db.Column(db.String(255), index=True, unique=True)
    chars = db.relationship('Character', backref='player', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.name)

class SkillPreqs(db.Model):
    skill_id = db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key = True)
    preq_id = db.Column('preq_id', db.Integer, db.ForeignKey('skill.id'), primary_key = True)
    skill = db.relationship('Skill', foreign_keys=[skill_id])
    preq = db.relationship('Skill', foreign_keys=[preq_id], back_populates='preqs')

    def __repr__(self):
        return '<Skill Prerequisite %r depends on %r>' % (self.skill, self.preq)

class CharSkills(db.Model):
    __tablename__ = 'char_skills'
    char_id = db.Column('char_id', db.Integer, db.ForeignKey('character.id'), primary_key = True)
    skill_id = db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key = True)
    skill_type = db.Column('skill_type', db.String(3))
    class_bonus = db.Column('class_bonus', db.Integer)
    inherited = db.Column('inherited', db.Boolean)
    lvl_added = db.Column('lvl_added', db.Integer)
    skill = db.relationship('Skill', back_populates='characters')
    character = db.relationship('Character', back_populates='skills')

    def __repr__(self):
        return '<CharSkill %r %r>' % (self.character, self.skill)

class SkillCategory(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    skills = db.relationship('Skill', backref='skills', lazy='dynamic')

    def __repr__(self):
        return '<Skill %r %r>' % (self.id, self.name)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique=True)
    description = db.Column(db.String())
    note =db.Column(db.String())
    skill_category = db.Column(db.Integer, db.ForeignKey('skill_category.id'))
    base = db.Column(db.Integer)
    per_level = db.Column(db.Integer)
    characters = db.relationship('CharSkills', back_populates='skill')
    preqs = db.relationship('SkillPreqs', foreign_keys=[SkillPreqs.skill_id])

    def __repr__(self):
        return '<Skill %r %r>' % (self.name, self.skill_category)

    # Used to render this object type for the flask.jsonify function
    def __html__(self):
        return '{"id": %r, "name": "%s"}' % (self.id, self.name)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    race = db.Column(db.String(150))
    occ = db.Column(db.String(150))
    sex = db.Column(db.String(1))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    age = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    sdc = db.Column(db.Integer)
    exp = db.Column(db.Integer)
    lvl = db.Column(db.Integer)
    iq = db.Column(db.Integer)
    me = db.Column(db.Integer)
    ma = db.Column(db.Integer)
    ps = db.Column(db.Integer)
    pp = db.Column(db.Integer)
    pe = db.Column(db.Integer)
    pb = db.Column(db.Integer)
    spd = db.Column(db.Integer)
    sav_sm = db.Column(db.Integer)
    sav_rm = db.Column(db.Integer)
    sav_psi = db.Column(db.Integer)
    sav_tp = db.Column(db.Integer)
    sav_hd = db.Column(db.Integer)
    sav_in = db.Column(db.Integer)
    sav_pos = db.Column(db.Integer)
    sav_hf = db.Column(db.Integer)
    sav_cd = db.Column(db.Integer)
    sav_pn = db.Column(db.Integer)
    alignment = db.Column(db.Integer, db.ForeignKey('alignment.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    skills = db.relationship('CharSkills', back_populates='character')

    @hybrid_property
    def calc_height(self):
        if self.height is not None and self.height > 0:
            feet = self.height / 12
            inches = self.height % 12
            return "%d Ft %d In" % (feet, inches)

    @hybrid_property
    def carry(self):
        #TODO:logic for strength type
        if (self.ps <= 16 and self.ps >= 3):
            return self.ps * 10
        elif (self.ps >= 17):
            return self.ps * 20
        else:
            return self.ps * 5

    @hybrid_property
    def lift(self):
        return self.carry * 2

    @hybrid_property
    def throw(self):
        # TODO: Logic for Strength type UG328
        return (self.carry/2, self.ps)

    @hybrid_property
    def run(self):
        return self.spd * 5

    @hybrid_property
    def run_mph(self):
        # 3600 is the number of feet / hour and 5280 is feet / mile
        return float(self.spd * 3600) / 5280

    def __repr__(self):
        return '<Character %r %r>' % (self.first_name, self.last_name)

class Alignment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(8))
    description = db.Column(db.String())
    chars = db.relationship('Character', backref='align', lazy='dynamic')

    def __repr__(self):
        return '<Alignment %r %r>' % (self.name, self.category)
