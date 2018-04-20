import json
from boat.boat_model import BoatModel
from slip.slip_model import SlipModel

#TODO: Need to add error coe to this
def delete_slip(event, context):
    slip = SlipModel.get(hash_key=event['pathParameters']['id'])
    # If boat contains a slip, set the boat at_sea to true
    if slip.current_boat:
        bid = slip.current_boat[-6:]
        boat = BoatModel.get(hash_key=bid)
        boat.update(actions=[BoatModel.at_sea.set(True)])

    sid = slip.id
    slip.delete()
    return {'statusCode': 200, 'body': json.dumps({ 'success': 'Slip {0} deleted'.format(sid), 'slip_id': sid })}
