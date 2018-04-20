import json
from boat.boat_model import BoatModel
from slip.slip_model import SlipModel

def delete_boat(event, context):
    boat = BoatModel(hash_key=event['pathParameters']['id'])
    bid = boat.id
    if boat.at_sea == True:
        slip = SlipModel.scan(filter_condition=(SlipModel.current_boat == '/boat/' + boat.id), limit=1)
        for s in slip:
            s.update(actions=[SlipModel.current_boat.remove(), SlipModel.arrival_date.remove()])
    
    boat.delete()
    return {'statusCode': 200, 'body': json.dumps({ 'success': 'Boat {0} deleted'.format(bid), 'boat_id': bid })}
