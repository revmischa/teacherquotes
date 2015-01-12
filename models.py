from teacherquotes import db
from flask.ext.sqlalchemy import SQLAlchemy

class School(db.Model):
    __tablename__ = 'schooldata'

    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String())
    teachers = db.relationship("Teacher", order_by='Teacher.lastname')

    def teacherCount(self):
        return len(self.teachers)

class Teacher(db.Model):
    __tablename__ = 'teacherdata'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    schoolid = db.Column(db.Integer(), db.ForeignKey("schooldata.id"))
    quotes = db.relationship("Quote", order_by='Quote.postdate')
    school = db.relationship("School", backref="teacherdata")

    def quoteCount(self):
        return len(self.quotes)


class Quote(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    poster = db.Column(db.String())
    rating = db.Column(db.Integer())
    quote = db.Column(db.String())
    postdate = db.Column(db.DateTime())
    teacherid = db.Column(db.Integer(), db.ForeignKey("teacherdata.id"))

    def quoteFixed(self):
        q = self.quote
        return q.replace("\\\\'", "'")
