import json
import logging
from slip.slip_model import SlipModel
from pynamodb.exceptions import DoesNotExist

def replace_slip(event, context):
    try:
        slip = SlipModel.get(hash_key=event['pathParameters']['id'])
    except DoesNotExist:
        return {'statusCode': 404, 'body': json.dumps({'error_message': 'SLIP was not found'})}
    
    slip_data = json.loads(event['body'])
    if 'number' not in slip_data:
        return {'statusCode': 422, 'body': json.dumps({'error_message': '\'number\' is only replaceable item. \'number\' requred.' })}

    if 'number' in slip_data:
        slip.number = slip_data['number']
    
    slip.save()
    return {'statusCode': 201, 'body': json.dumps(dict(slip))}
