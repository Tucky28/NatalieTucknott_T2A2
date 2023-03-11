from main import db

class Invoice(db.Model):
    __tablename__ = 'invoices'
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    supplier_name = db.Column(db.String(255), nullable=False)

    # Define relationships
    business = db.relationship('Business', backref='invoices_business'('finance_agreements', lazy=True))