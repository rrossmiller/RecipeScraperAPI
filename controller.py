from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from scraper import halfBakedHarvest
app = Flask(__name__)
# app.debug = True
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
api = Api(app)
parser = reqparse.RequestParser()

class RecipeScraper(Resource):
    def get(self):
        parser.add_argument('recipe', type=str, help='Link to the recipe')
        recipeLink = parser.parse_args()['recipe']
        ingredients = halfBakedHarvest(recipeLink)
        return {'ingredients':ingredients}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(RecipeScraper, '/halfBakedHarvest')
api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(host='0.0.0.0')