import json
from pynamodb.exceptions import DoesNotExist, ScanError
from boat.boat_model import BoatModel
from slip.slip_model import SlipModel

def boat_departure(event, context):
    try:
        boat = BoatModel.get(hash_key=event['pathParameters']['id'])
    except DoesNotExist:
        return {'statusCode': 404, 'body': json.dumps({'error_message': 'BOAT was not found'})}

    try:
        # Scan for boat in slip
        slip = SlipModel.scan(filter_condition=(SlipModel.current_boat == '/boat/' + boat.id), limit=1)
    except ScanError: # If scan fails return
        return {'statusCode': 404, 'body': json.dumps({'error message': 'Slip not found'})} # Don't need this
    
    # If not slip return
    # if slip.total_count == 0:
    #     return {'statusCode': 404, 'body': json.dumps({'error message': 'BOAT not in slip'})} 

    # Set to 'at sea'
    boat.update(actions=[BoatModel.at_sea.set(True)])
    for s in slip:
        s.update(actions=[SlipModel.current_boat.remove(), SlipModel.arrival_date.remove()])
        return { 'statusCode': 200, 'body': json.dumps({'success': 'Boat {0} departed slip {1}'.format(boat.id, s.id), 'slip_id': '{0}'.format(s.id), 'boat_id': '{0}'.format(boat.id) })}