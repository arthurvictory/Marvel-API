from flask import Blueprint, request, jsonify
from superhero_inventory.helpers import token_required
from superhero_inventory.models import db, Superhero, superhero_schema, superheroes_schema


api = Blueprint('api', __name__, url_prefix = '/api')


@api.route('/getdata')
def getdata():
    return {'some': 'value'}


@api.route('/superheroes', methods = ['POST'])
@token_required
def create_superhero(our_user):

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    appeared = request.json['appeared']
    superpowers = request.json['superpowers']
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    superhero = Superhero(name, description, price, appeared, superpowers, user_token)

    db.session.add(superhero)
    db.session.commit()

    response = superhero_schema.dump(superhero)

    return jsonify(response)

# Read 1 Superhero Endpoint
@api.route('/superheroes/<id>', methods = ['GET'])
@token_required
def get_superhero(our_user, id):
    if id:
        superhero = Superhero.query.get(id)
        response = superhero_schema.dump(superhero)
        return jsonify(response)
    else:
        return jsonify({'message': 'ID is missing'}), 401
    
# Read all the superheroes endpoint
@api.route('/superheroes', methods = ['GET'])
@token_required
def get_superheroes(our_user):
    token = our_user.token
    superheroes = Superhero.query.filter_by(user_token = token).all()
    response = superheroes_schema.dump(superheroes)

    return jsonify(response)

# Update 1 Superhero by ID
@api.route('/superhero/<id>', methods = ['PUT'])
@token_required
def update_superhero(our_user, id):
    superhero = Superhero.query.get(id)

    superhero.name = request.json['name']
    superhero.description = request.json['description']
    superhero.price = request.json['price']
    superhero.appeared = request.json['appeared']
    superhero.superpowers = request.json['superpowers']
    superhero.user_token = our_user.token

    db.session.commit()

    response = superhero_schema.dump(superhero)

    return jsonify(response)

# Delete 1 Superhero by ID
@api.route('/superhero/<id>', methods = ['DELETE'])
@token_required
def delete_superhero(our_user, id):
    superhero = Superhero.query.get(id)
    db.session.delete(superhero)
    db.session.commit()

    response = superhero_schema.dump(superhero)

    return jsonify(response)