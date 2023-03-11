from app import db

class CreditTier(db.Model):
    __tablename__ = 'credit_tiers'
    id = db.Column(db.Integer, primary_key=True)
    tier_level = db.Column(db.Integer, nullable=False)
    min_credit_score = db.Column(db.Integer, nullable=False)
    max_credit_score = db.Column(db.Integer, nullable=False)
