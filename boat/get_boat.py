import json
from pynamodb.exceptions import DoesNotExist
from boat.boat_model import BoatModel


def get_boat(event, context):
    try:
        boat = BoatModel.get(hash_key=event['pathParameters']['id'])
    except DoesNotExist:
        return {'statusCode': 404, 'body': json.dumps({'error_message': 'BOAT was not found'})}

    # Print boat
    return {'statusCode': 200, 'body': json.dumps(dict(boat))}
