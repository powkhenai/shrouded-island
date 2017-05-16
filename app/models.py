from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    login_token = db.Column(db.String(255), index=True, unique=True)
    chars = db.relationship('Character', backref='player', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.name)

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

    def __repr__(self):
        return '<Character %r %r>' % (self.first_name, self.last_name)
