import json
from pynamodb.exceptions import DoesNotExist
from slip.slip_model import SlipModel

def get_slip(event, context):
    try:
        slip = SlipModel.get(hash_key=event['pathParameters']['id'])
    except DoesNotExist:
        return {'statusCode': 404, 'body': json.dumps({'error_message': 'SLIP was not found'})}
    return {'statusCode': 200, 'body': json.dumps(dict(slip))}
