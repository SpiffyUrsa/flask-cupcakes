"""Flask app for Cupcakes"""


from flask import Flask, request, redirect, render_template, flash, jsonify
# from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# debug = DebugToolbarExtension(app)

@app.route("/api/cupcakes")
def list_all_cupcakes():

    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]
    # For each instance of cupcake, we serialize(turn into a dict) each instance of cupcake. 

    return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes/<int:cupcake_id>")
def list_single_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.route("/api/cupcakes", methods=['POST'])
def create_cupcake():

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"] or None

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    flavor = cupcake.flavor
    size = cupcake.size
    rating = cupcake.rating
    image = cupcake.image

    #turn this into a loop :)

    try:
        cupcake.flavor = request.json["flavor"]
    except KeyError:
        cupcake.flavor = flavor
    try:
        cupcake.size = request.json["size"]
    except KeyError:
        cupcake.size = size
    try:
        cupcake.rating = request.json["rating"]
    except KeyError:
        cupcake.rating = rating
    try:
        cupcake.image = request.json["image"]
    except KeyError:
        cupcake.image = image

    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 200)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return (jsonify(message='Deleted'), 200)
 

