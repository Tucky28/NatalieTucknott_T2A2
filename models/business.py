from main import db

class Business(db.Model):
    __tablename__ = 'businesses'
    id = db.Column(db.Integer, primary_key=True)
    ABN = db.Column(db.Integer, nullable=False, unique=True)
    business_name = db.Column(db.String(255), nullable=False)
    credit_score = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    credit_tier_id = db.Column(db.Integer, db.ForeignKey('credit_tiers.id'), nullable=False)

    # Define relationships
    credit_tier = db.relationship('CreditTier', backref='businesses')