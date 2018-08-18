from app import db

class BalanceModel(db.Model):
    __tablename__ = 'balances'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True)
    amount = db.Column(db.Integer)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def add(self, amount):
        self.amount += amount
        self.save_to_db()

    def charge(self, amount):
        self.amount -= amount
        self.save_to_db()

    def __str__(self):
        return '{} : {}'.format(self.username, str(self.amount))
