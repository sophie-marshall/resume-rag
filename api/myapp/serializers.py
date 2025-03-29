from rest_framework import serializers
from .models import SampleModel

# this allows the database content to be returned as JSON
class SampleModelSerializer(serializers.ModelSerializer):
    # tell django how to handle the models serialization
    class Meta:
        # this links the current serializer to the SampleModel
        model = SampleModel
        # defines the fiels to be included (id is auto generated)
        fields = ['id', 'title', 'content', 'date']