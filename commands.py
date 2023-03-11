from main import db, create_app
from flask import Blueprint
from models.credit_tiers import CreditTier

db_commands = Blueprint("db", __name__)

@db_commands.cli.command('drop')
def drop_db():
    # Tell SQLAlchemy to drop all tables
    db.drop_all()
    print('Tables dropped')

@db_commands.cli.command('seed')
def seed_db():

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
    
    print("tables seeded")