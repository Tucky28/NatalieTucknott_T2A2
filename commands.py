from main import db
from main import bcrypt
from flask import Blueprint
from models.credit_tiers import CreditTier
from models.business import Business
from models.products import Product
from models.invoice import Invoice
from models.finance_agreement import FinanceAgreement
import datetime

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create_tables")
def create_tables():
    # Create the tables
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Dropped the database")

@db_commands.cli.command('seed')
def seed_db():
    # Create credit tiers
    credit_tiers = [
        CreditTier(tier_level=1, min_credit_score=300, max_credit_score=579),
        CreditTier(tier_level=2, min_credit_score=580, max_credit_score=669),
        CreditTier(tier_level=3, min_credit_score=670, max_credit_score=739),
        CreditTier(tier_level=4, min_credit_score=740, max_credit_score=799),
        CreditTier(tier_level=5, min_credit_score=800, max_credit_score=850)
    ]
    for tier in credit_tiers:
        db.session.add(tier)
        db.session.commit()

    # Create businesses
    hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')

    businesses = [    
        Business(ABN=1234567890, business_name='Business One', credit_score=600, email='business1@example.com', password=hashed_password,),    
        Business(ABN=2345678901, business_name='Business Two', credit_score=700, email='business2@example.com', password=hashed_password,),    
        Business(ABN=3456789012, business_name='Business Three', credit_score=550, email='business3@example.com', password=hashed_password,)
    ]

    for business in businesses:
        db.session.add(business)
        db.session.commit()

    # Loop through the businesses and assign credit tiers based on their credit scores
    for i, business in enumerate(businesses):
        credit_score = business.credit_score
        for tier in credit_tiers:
            if tier.min_credit_score <= credit_score <= tier.max_credit_score:
                businesses[i].credit_tier_id = tier.id
                break

    # Update the businesses table with the credit tier assignments
    for business in businesses:
        business_obj = Business.query.filter_by(ABN=business.ABN).first()
        business_obj.credit_tier_id = business.credit_tier_id
        db.session.add(business_obj)

    # Commit the changes to the database
    db.session.commit()
    
    credit_tier_1 = CreditTier.query.filter_by(tier_level=1).first()
    credit_tier_2 = CreditTier.query.filter_by(tier_level=2).first()
    credit_tier_3 = CreditTier.query.filter_by(tier_level=3).first()

    # Create products
    products = [
        Product(repayment_term=3, fee=4.0, installment_term=1, product_credit_tier=credit_tier_1.id),
        Product(repayment_term=24, fee=6.0, installment_term=2, product_credit_tier=credit_tier_2.id),
        Product(repayment_term=36, fee=8.0, installment_term=3, product_credit_tier=credit_tier_3.id),
    ]
    for product in products:
        db.session.add(product)
        db.session.commit()

    # Create invoices
    invoices = [
        Invoice(business_id=businesses[0].id, due_date=datetime.date(2022, 3, 31), amount=2500.56, supplier_name='Supplier A'),
        Invoice(business_id=businesses[1].id, due_date=datetime.date(2022, 4, 30), amount=5000.99, supplier_name='Supplier B'),
        Invoice(business_id=businesses[2].id, due_date=datetime.date(2022, 5, 31), amount=7500.34, supplier_name='Supplier C')
    ]

    for invoice in invoices:
        db.session.add(invoice)
        db.session.commit()
    print("Tables seeded")
    