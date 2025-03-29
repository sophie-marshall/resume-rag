from rest_framework import serializers 
from .models import Documents

class DocumentModelSerializer(serializers.ModelSerializer):
    class Meta:
        # link model 
        model = Documents
        fields = ['uuid', 'document_id', 'chunk_id', 'clean_text', 'tags', 'embedding']