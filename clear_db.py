import json
from pynamodb.exceptions import DoesNotExist
from entity_type_gsi import EntityType
from boat.boat_model import BoatModel
from slip.slip_model import SlipModel

# This is a special request that clears the database for the purposes of testing.
def clear_db(event, context):
    # Get all of the boats and slips
    boats = BoatModel.scan(filter_condition=(BoatModel.entity_type == 'boat'))
    slips = SlipModel.scan(filter_condition=(SlipModel.entity_type == 'slip'))

    # And delete them 
    for s in slips:
        s.delete()
    for b in boats:
        b.delete()
    
    return {'statusCode': 200, 'body': json.dumps({'boats': [dict(boat) for b in boats], 'slips': [dict(slip) for s in slips] })}
    
