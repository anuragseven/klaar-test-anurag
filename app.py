from flask import Flask
from flask_restful import Api, reqparse
import dbconnect as db

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
api = Api(app)

arg_parser = reqparse.RequestParser()
arg_parser.add_argument("query", type=str, help="send proper query ", required=True)
arg_parser.add_argument("limit", type=int, help="send valid limit ", required=True)
arg_parser.add_argument("offset", type=int, help="send valid offset", )


@app.route('/api/branches/autocomplete', methods=['GET'])
def autocomplete():
    try:
        args = arg_parser.parse_args()
        query = args['query']
        limit = args['limit']
        offset = args['offset']

        if offset is not None:
            return db.getAllRowsWithMachingBranches(query, limit, offset)
        else:

            return db.getAllRowsWithMachingBranches(query, limit)
    except Exception as e:
        return {'error': 'error occured while fetching branches', 'description': str(e)}, 400


@app.route('/api/branches', methods=['GET'])
def search():
    try:
        args = arg_parser.parse_args()
        query = args['query']
        limit = args['limit']
        offset = args['offset']

        if offset is not None:
            return db.getAllRowsWithMachingQuery(query, limit, offset)
        else:

            return db.getAllRowsWithMachingQuery(query, limit)
    except Exception as e:
        return {'error': 'error occured while fetching branches', 'description': str(e)}, 400


@app.route('/', methods=['GET'])
def home():
    return "Anurag Tripathi Klaar BE Test"


if __name__ == "__main__":
    app.run()
