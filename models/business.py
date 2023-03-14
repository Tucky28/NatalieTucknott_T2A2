from main import db
from marshmallow import fields, Schema

class Business(db.Model):
    __tablename__ = 'businesses'
    id = db.Column(db.Integer, primary_key=True)
    ABN = db.Column(db.BigInteger, nullable=False, unique=True)
    business_name = db.Column(db.String(255), nullable=False)
    credit_score = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    credit_tier_id = db.Column(db.Integer, db.ForeignKey('credit_tiers.id'), nullable=True)

class BusinessSchema(Schema):
    id = fields.Integer(dump_only=True)
    ABN = fields.Integer(required=True)
    business_name = fields.String(required=True)
    credit_score = fields.Integer(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    credit_tier_id = fields.Integer()
