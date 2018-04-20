import json
import pytz
from datetime import datetime
from scancount import scancount
from pynamodb.exceptions import DoesNotExist, ScanError
from boat.boat_model import BoatModel
from slip.slip_model import SlipModel
from entity_type_gsi import EntityType

path = 'https://coffeetilnoon.com/'
def boat_arrival(event, context):
    try: # get boat
        boat = BoatModel.get(hash_key=event['pathParameters']['id'])
    except DoesNotExist: # if not found then 'not found'
        return {'statusCode': 404, 'body': json.dumps({'error_message': 'BOAT was not found'})}
    
    # sc = EntityType.count(hash_key='entity_type', filter_condition=SlipModel.current_boat.does_not_exist() & (SlipModel.entity_type == 'slip'))
    # sc = SlipModel.e_type.count(hash_key='entity_type', filter_condition=SlipModel.current_boat.does_not_exist() & (SlipModel.entity_type == 'slip'))
    try:
        # scan for empty slip. Only need one so limited to one result
        # slip = SlipModel.query(filter_condition=SlipModel.current_boat.does_not_exist() & (SlipModel.entity_type == 'slip'), limit=1)

        slip = SlipModel.scan(filter_condition=SlipModel.current_boat.does_not_exist() & (SlipModel.entity_type == 'slip'), limit=1)
    except DoesNotExist:
        return {'statusCode': 403, 'body': json.dumps({'error message': 'No slips found'})}


    boat.update(actions=[BoatModel.at_sea.set(False)]) # set boat at_sea to false
    for s in slip:
        if s.count > 0:
            s.update(actions=[SlipModel.current_boat.set('/boat/' + boat.id), SlipModel.arrival_date.set(str(datetime.now()))])
            b = path + boat.id
            return { 'statusCode': 200, 'body': json.dumps({'success': 'Boat {0} arrived in slip {1}'.format(b, s.id), 'slip': dict(s) }) }
        else:
            return {'statusCode': 403, 'body': json.dumps({'error message': 'No empty slips'})}
    

