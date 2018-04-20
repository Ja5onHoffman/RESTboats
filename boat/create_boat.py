import json
import logging
import uuid

from boat.boat_model import BoatModel
from create_id import create_id

def create(event, context):
    boat_data = json.loads(event['body'])
    if 'name' not in boat_data:
        logging.error('Validation Failed')
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the new boat.'})}

    if not boat_data['name']:
        logging.error('Validation Failed - boat name was empty. %s', boat_data)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the boat. Name was empty'})}

    new_boat = BoatModel()
    new_boat.id = create_id()
    if 'name' in boat_data:
        new_boat.name = boat_data['name']
    if 'type' in boat_data:
        new_boat.type = boat_data['type']
    if 'length' in boat_data:
        new_boat.length = boat_data['length']
    if 'at_sea' in boat_data:
        new_boat.at_sea = boat_data['at_sea']

    # write the new boat to the database
    new_boat.save()

    # create a response
    return {'statusCode': 201, 'body': json.dumps(dict(new_boat))}

