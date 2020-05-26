from flask import Flask
from flask_restful import Resource, Api, reqparse
from scraper import halfBakedHarvest
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

class RecipeScraper(Resource):
    def get(self):
        parser.add_argument('recipe', type=str, help='Link to the recipe')
        recipeLink = parser.parse_args()['recipe']
        ingredients = halfBakedHarvest(recipeLink)
        return {'ingredients': ingredients}

api.add_resource(RecipeScraper, '/')

if __name__ == '__main__':
    app.run(debug=True)
    # app.run()