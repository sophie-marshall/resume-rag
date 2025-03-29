from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SampleModel
from .serializers import SampleModelSerializer

# ModelViewSet will give you standard HTTP protocols out of the box
class SampleModelViewSet(viewsets.ModelViewSet):
    # set app permissions 
    premission_classes = [IsAuthenticated]
    # define the data to retrieve from the database, in this case all instances
    queryset = SampleModel.objects.all()
    # tell django how to convert the model into JSON format (and vice versa)
    serializer_class = SampleModelSerializer

    
    @action(detail=True, methods=['post'])
    # defintione an action called "custom_action"
    def custom_action(self, request, pk=None):
        samplemodel = self.get_object()
        # logic to do somethign 
        return Response({'status': 'custom action triggered'})
