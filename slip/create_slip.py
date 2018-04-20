import json
import logging
import uuid
import random

from slip.slip_model import SlipModel
from create_id import create_id

def create(event, context):
    slip_data = json.loads(event['body'])

    new_slip = SlipModel()
    new_slip.id = create_id()
    if 'number' in slip_data:
        new_slip.number = slip_data['number']
    else: # If no number provided just generate one
        new_slip.number = random.randint(1,100)
    
    # write the slip to the database
    new_slip.save()

    # create a response
    return {'statusCode': 201, 'body': json.dumps(dict(new_slip))}

