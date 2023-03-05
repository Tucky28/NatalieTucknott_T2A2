from main import db

class CreditTier(db.Model):
    __tablename__ = 'credit_tier'
    id = db.Column(db.Integer, primary_key=True)
    tier_level = db.Column(db.Integer)
    min_credit_score = db.Column(db.Integer)
    max_credit_score = db.Column(db.Integer)