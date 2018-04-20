import os
from datetime import datetime
from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute, NumberAttribute
from pynamodb.models import Model
from entity_type_gsi import EntityType

class BoatModel(Model):
    class Meta:
        table_name = os.environ['DYNAMODB_TABLE'] 
        if 'ENV' in os.environ:
            host = 'http://localhost:8000'  
        else:
            region = 'us-east-1'

    id = UnicodeAttribute(hash_key=True, null=False)
    name = UnicodeAttribute(null=False)
    type = UnicodeAttribute(hash_key=False, null=False)
    length = NumberAttribute(hash_key=False, range_key=False, null=None, default=0)
    at_sea = BooleanAttribute(hash_key=False, range_key=False, null=None, default=True)
    e_type = EntityType()
    entity_type = UnicodeAttribute(default='boat')

    def save(self, conditional_operator=None, **expected_values):
        self.updatedAt = datetime.now()
        super(BoatModel, self).save()

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))