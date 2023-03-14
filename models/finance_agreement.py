from main import db

class FinanceAgreement(db.Model):
    __tablename__ = 'finance_agreements'
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    fee_amount = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    
    # Define relationships
    invoice = db.relationship('Invoice', backref='finance_agreements')
    product = db.relationship('Product', backref='finance_agreements')
