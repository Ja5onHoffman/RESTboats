
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.attributes import UnicodeAttribute

# GSI for querying all boats/slips
# The entity_type attribute was a helpful addition for AWS but not
# part of the assignment

class EntityType(GlobalSecondaryIndex):
    class Meta:
        # index_name is optional, but can be provided to override the default name
        index_name = 'entity_type'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    # This attribute is the hash key for the index
    # Note that this attribute must also exist
    # in the model
    entity_type = UnicodeAttribute(default='', hash_key=True) #change the name of this so they aren't both called gsi_id