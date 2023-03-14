from main import db
from marshmallow import Schema, fields

class CreditTier(db.Model):
    __tablename__ = 'credit_tiers'
    id = db.Column(db.Integer, primary_key=True)
    tier_level = db.Column(db.Integer, nullable=False)
    min_credit_score = db.Column(db.Integer, nullable=False)
    max_credit_score = db.Column(db.Integer, nullable=False)

class CreditTierSchema(Schema):
    id = fields.Integer(dump_only=True)
    tier_level = fields.Integer(required=True)
    min_credit_score = fields.Integer(required=True)
    max_credit_score = fields.Integer(required=True)

class ManyCreditTiersSchema(Schema):
    credit_tiers = fields.Nested(CreditTierSchema, many=True)
