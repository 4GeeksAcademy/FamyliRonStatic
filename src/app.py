"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson") 

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



@app.route('/members', methods=['GET'])
def handle_GET():
        members = jackson_family.get_all_members()
        response_body = {"hello": "world",
                         "family": members}
        return response_body, 200

@app.route('/members', methods=['POST'])
def handle_POST():
        data = request.json
        response_body = {}
        print(data)
        jackson_family.add_member(data)
        members = jackson_family.get_all_members()
        response_body["message"] = "Add it!"
        response_body["results"] = members
        return response_body, 200


    
@app.route('/members/<int:id_member>', methods=['GET'])
def handle_member(id_member):
    response_body = {}
    member = jackson_family.get_member(id_member)
    if member:
            response_body['message'] = 'Found it!'
            response_body['results'] = member
            return jsonify(response_body), 200
    else:
            response_body = {'message': 'Cant be found it...',
                             'results': []}
    return response_body, 404
    
@app.route('/members/<int:id_member>', methods=["DELETE"])
def handle_elimin(id_member):
    response_body = {}
    member = jackson_family.delete_member(id_member)
    if member:
        response_body['message'] = 'Delete it!'
        response_body['results'] = "Deleteado"
        return response_body, 200
    else:
        response_body = {'message': 'Cant be delete it...',
                        'results': []} 
    return jsonify(response_body), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
