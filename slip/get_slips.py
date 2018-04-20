import json
from pynamodb.exceptions import DoesNotExist
from entity_type_gsi import EntityType
from slip.slip_model import SlipModel


def get_slips(event, context):
    try:
        slips = SlipModel.scan(filter_condition=(SlipModel.entity_type == 'slip'))
    except DoesNotExist:
        return {'statusCode': 404, 'body': json.dumps({'error_message': 'No slips in table'})}

    return {'statusCode': 200, 'body': json.dumps({'slips': [dict(slip) for slip in slips]})}