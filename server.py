from flask import Flask, request, jsonify
from json import dumps, loads
from restaurants import closest_venues
from werkzeug.exceptions import HTTPException

class InputError(HTTPException):
    code = 400
    message = 'No message specified'

APP = Flask(__name__)

@APP.route("/restaurants", methods=['GET'])
def get_closest_venues():
    
    try: 
        lat = float(request.args.get('latitude'))
        long = float(request.args.get('longitude'))
    except (ValueError, TypeError):
        raise InputError("Invalid Latitude or Longitude Provided")

    limit = request.args.get('limit')

    if limit is None:
        limit = 10  # default limit value
    else:
        try:
            limit = int(limit)
        except ValueError:
            raise InputError("Invalid Limit Provided")

    venues = closest_venues(lat, long, limit)
    return dumps(venues) 

if __name__ == '__main__':
    APP.run(debug=True)
