from app import db


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, index=True, unique=True)
    date = db.Column(db.Date, index=True)
    time = db.Column(db.Time, index=True)

    def __repr__(self):
        return f'<Ticket {self.number}>'
