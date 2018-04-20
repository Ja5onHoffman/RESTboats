import logging
import uuid
import json
from slip.slip_model import SlipModel
from pynamodb.exceptions import DoesNotExist

def mod_slip(event, context):
    try:
        slip = SlipModel.get(hash_key=event['pathParameters']['id'])
    except DoesNotExist:
        return {'statusCode': 404, 'body': json.dumps({'error_message': 'SLIP was not found'})}

    # slip number is the only modifiable thing right now
    slip_data = json.loads(event['body'])
    if 'number' in slip_data:
        slip.number = slip_data['number']


    slip.save()
    return {'statusCode': 200, 'body': json.dumps(dict(slip))}



