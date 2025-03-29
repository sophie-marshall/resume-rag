from django.shortcuts import render
import rest_framework
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Documents
from .serializers import DocumentModelSerializer
from .utils import embed_clean_text
import logging

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Log everything, including DEBUG level messages

# Create your views here.
class DocumentModelViewSet(rest_framework.viewsets.ModelViewSet):
    permission_classes = [rest_framework.permissions.IsAuthenticated]
    queryset = Documents.objects.all()
    serializer_class = DocumentModelSerializer
