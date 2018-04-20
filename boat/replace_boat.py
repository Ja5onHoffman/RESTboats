import json
import logging
from boat.boat_model import BoatModel

def replace_boat(event, context):
    boat = BoatModel.get(hash_key=event['pathParameters']['id'])
    boat_data = json.loads(event['body'])
    if 'name' not in boat_data:
        logging.error('Validation Failed')
        return {'statusCode': 422, 'body': json.dumps({'error_message': 'Couldn\'t create the new boat.'})}

    if not boat_data['name']:
        logging.error('Validation Failed - boat name was empty. %s', boat_data)
        return {'statusCode': 422, 'body': json.dumps({'error_message': 'Couldn\'t create the boat. Name was empty'})}

    if 'name' in boat_data:
        boat.name = boat_data['name']
    if 'type' in boat_data:
        boat.type = boat_data['type']
    if 'length' in boat_data:
        boat.length = boat_data['length']
    # No 'at_sea'

    # write the boat to the database
    boat.save()

    # create a response
    return {'statusCode': 201, 'body': json.dumps(dict(boat))}

