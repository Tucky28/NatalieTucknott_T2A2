from models.business import BusinessSchema
from flask import Blueprint, jsonify, request
from models.business import Business
from main import db
from models.credit_tiers import CreditTier
from flask_bcrypt import bcrypt

businesses = Blueprint('businesses', __name__, url_prefix="/businesses")

# Define the endpoint for getting a single business by ID
@businesses.route('/<int:business_id>', methods=['GET'])
def get_single_business(business_id):
    # Find the business with the given ID, or return a 404 error if it doesn't exist
    business = Business.query.get_or_404(business_id)

    # Create a BusinessSchema object and serialize the business as JSON
    business_schema = BusinessSchema()
    result = business_schema.dump(business)

    # Return the serialized business as JSON
    return jsonify(result)

# Define the endpoint for getting all businesses
@businesses.route('/', methods=['GET'])
def get_all_businesses():
    # Retrieve all businesses from the database
    businesses = Business.query.all()

    # Create a BusinessSchema object and serialize all the businesses as JSON
    businesses_schema = BusinessSchema(many=True)
    results = businesses_schema.dump(businesses)

    # Return the serialized businesses as JSON
    return jsonify(results)

@businesses.route('/create', methods=['POST'])
def create_business():
    # Parse the JSON data from the request body
    business_data = BusinessSchema().load(request.json)

    # Hash the password using bcrypt
    password = request.json.get('password')
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    business = Business(
        ABN=business_data["ABN"],
        business_name=business_data["business_name"],
        email=business_data["email"],
        credit_score=business_data["credit_score"],
        password=hashed_password.decode('utf-8'),
    )

    # Extract the credit score from the request
    credit_score = request.json.get('credit_score')

    # Query the credit tiers table to get the matching credit tier
    credit_tier = CreditTier.query.filter(CreditTier.min_credit_score <= credit_score,
                                          CreditTier.max_credit_score >= credit_score).first()

    # If a matching credit tier is found, assign it to the credit_tier_id field
    if credit_tier:
        business.credit_tier_id = credit_tier.id
    
    # Load the data into a Business object and validate it
    errors = BusinessSchema().validate(business_data)
    if errors:
        return jsonify(errors), 422

    # Add the business to the database
    db.session.add(business)
    db.session.commit()

    # Serialize the business object and return it as JSON
    result = BusinessSchema().dump(business)
    return jsonify(result), 201

# Define the endpoint for deleting a business
@businesses.route('/delete/<int:id>', methods=['DELETE'])
def delete_business(id):
    # Find the business in the database
    business = Business.query.get(id)

    # If the business doesn't exist, return a 404 error
    if not business:
        return jsonify({'error': 'Business not found'}), 404

    # Check if there are any invoices associated with the business
    if business.invoices:
        return jsonify({'error': 'Cannot delete a business with associated invoices'}), 400

    # Delete the business from the database
    db.session.delete(business)
    db.session.commit()

    return 'Successfully Deleted', 204

# Define the endpoint for editing a business
@businesses.route('/update/<int:id>', methods=['PUT'])
def edit_business(id):
    # Find the business in the database
    business = Business.query.get(id)

    # If the business doesn't exist, return a 404 error
    if not business:
        return jsonify({'error': 'Business not found'}), 404

    # Parse the JSON data from the request body
    data = request.get_json()

    # Deserialize the data into a Business object
    business = BusinessSchema().load(data, instance=business, partial=True)

    # Save the changes to the database
    db.session.commit()

    # Serialize the business object and return it as JSON
    result = BusinessSchema().dump(business)
    return jsonify(result)
