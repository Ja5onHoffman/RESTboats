import os
from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute, NumberAttribute
from pynamodb.models import Model
from entity_type_gsi import EntityType


# Should just name this Slip
class SlipModel(Model):
    class Meta:
        table_name = os.environ['DYNAMODB_TABLE'] # just use table name here
        if 'ENV' in os.environ:
            host = 'http://localhost:8000'  
        else:
            region = 'us-east-1'
            # change to own link
            # host = 'https://dynamodb.eu-central-1.amazonaws.com'
    
    id = UnicodeAttribute(hash_key=True, null=False)
    number = NumberAttribute(hash_key=False, range_key=False, null=None)
    current_boat = UnicodeAttribute(hash_key=False, null=True)
    arrival_date = UnicodeAttribute(hash_key=False, null=True)
    e_type = EntityType()
    entity_type = UnicodeAttribute(default='slip')
    # departure_history - EC. Do later

    def save(self, conditional_operator=None, **expected_values):
        self.updatedAt = datetime.now()
        super(SlipModel, self).save()

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))