import logging
import uuid
import json
from boat.boat_model import BoatModel
from pynamodb.exceptions import DoesNotExist

def mod_boat(event, context):
    try:
        boat = BoatModel.get(hash_key=event['pathParameters']['id'])
    except DoesNotExist:
        return {'statusCode': 404, 'body': json.dumps({'error_message': 'BOAT was not found'})}
    
    # Decided not to allow at_sea to be changed here
    # at_sea_changed = False
    boat_data = json.loads(event['body'])
    if 'name' in boat_data:
        boat.name = boat_data['name']
    if 'type' in boat_data:
        boat.type = boat_data['type']
    if 'length' in boat_data:
        boat.length = boat_data['length']
    # if 'at_sea' in boat_data:
    #     boat.at_sea = boat_data['at_sea']
    #     at_sea_changed = True


    boat.save()
    # Leaving this out
    # if at_sea_changed:
    #     try:
    #     # scan for empty slip. Only need one so limited to one result
    #     # slip = SlipModel.query('current_boat', SlipModel.current_boat.contains(boat.id))
    #         slip = SlipModel.scan(filter_condition=(SlipModel.current_boat == '/boat/' + boat.id), limit=1)
    #     for s in slip:
    #         s.update(actions=[SlipModel.current_boat.remove(), SlipModel.arrival_date.remove()])
    #         return {'statusCode': 200, 'body': json.dumps(dict(boat)), {'note': 'at_sea attribute changed'}}
    # if at_sea_changed:
    #     return {'statusCode': 200, 'body': json.dumps(dict(boat)), {'WARNING': 'at_sea attribute changed. \
    #                             Use \'DELETE /boat/{id}/slip\' when changing this status. Boat {0} still ' }}
    return {'statusCode': 200, 'body': json.dumps(dict(boat))}



