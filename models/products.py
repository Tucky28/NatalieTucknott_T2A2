from main import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    repayment_term = db.Column(db.Integer, nullable=False)
    fee = db.Column(db.Float, nullable=False)
    installment_term = db.Column(db.Integer, nullable=False)
    product_credit_tier = db.Column(db.Integer, db.ForeignKey("credit_tiers.id"), nullable=False)

    #  Define relationship
    credit_tier = db.relationship('CreditTier', backref='products')