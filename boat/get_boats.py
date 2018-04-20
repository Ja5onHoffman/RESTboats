import json
from pynamodb.exceptions import DoesNotExist
from entity_type_gsi import EntityType
from boat.boat_model import BoatModel


def get_boats(event, context):
    try:
        boats = BoatModel.scan(filter_condition=(BoatModel.entity_type == 'boat'))
        # for b in BoatModel.scan(filter_condition=(BoatModel.entity_type ==))
    except DoesNotExist:
        return {'statusCode': 404,
                    'body': json.dumps({'error_message': 'No boats in table'})}
    # Print all boats
    return {'statusCode': 200, 'body': json.dumps({'boats': [dict(boat) for boat in boats]})}


