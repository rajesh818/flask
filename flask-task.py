# using flask_restful
from flask import Flask, request, abort, jsonify
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)
class SendData(Resource):
    def get(self,name):
        path = "database/" + name + ".json"
        try:
            with open(path) as file_data:
                    file_data = json.load(file_data)
        except Exception as error:
            abort(404)
        return file_data

class ReceiveData(Resource):
    def post(self,name):
        path = "database/" + name + ".json"
        data = request.get_json()
        json_object = json.dumps(data, indent = 4)
        try:
            with open(path, "w") as outfile:
                outfile.write(json_object)
        except Exception as error:
            abort(404)
        return jsonify({"status" : "successfully added"})

api.add_resource(SendData, '/get/<string:name>')
api.add_resource(ReceiveData, '/add/<string:name>')

if __name__ == '__main__':
	app.run(debug = True)