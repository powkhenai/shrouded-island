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

class CharSkills(db.Model):
        __tablename__ = 'char_skills'
        char_id = db.Column('char_id', db.Integer, db.ForeignKey('character.id'), primary_key = True)
        skill_id = db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key = True)
        skill_type = db.Column('skill_type', db.String(3))

class SkillCategory(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    skills = db.relationship('Skill', backref='skills', lazy='dynamic')

    def __repr__(self):
        return '<Skill %r %r>' % (self.id, self.name)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150))
    description = db.Column(db.String())
    note =db.Column(db.String())
    skill_category = db.Column(db.Integer, db.ForeignKey('skill_category.id'))
    base = db.Column(db.Integer)
    per_level = db.Column(db.Integer)

    def __repr__(self):
        return '<Skill %r %r>' % (self.name, self.skill_category)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    age = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    exp = db.Column(db.Integer)
    iq = db.Column(db.Integer)
    me = db.Column(db.Integer)
    ma = db.Column(db.Integer)
    ps = db.Column(db.Integer)
    pp = db.Column(db.Integer)
    pe = db.Column(db.Integer)
    pb = db.Column(db.Integer)
    spd = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    skills = db.relationship('Skill', secondary='char_skills', backref=db.backref('characters', lazy='dynamic'))

    def __repr__(self):
        return '<Character %r %r>' % (self.first_name, self.last_name)
