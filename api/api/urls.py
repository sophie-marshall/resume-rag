"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import SampleModelViewSet
from rag.views import DocumentModelViewSet

## -- SAMPLE ROUTER -- ##
# create an instance of DRF router to automatically generate RESTful URL patterns
sample_router = DefaultRouter()
# connect a viewset to the URL pattern
sample_router.register(r'samplemodel', SampleModelViewSet)

## -- RAG ROUTER -- ##
rag_router = DefaultRouter()
rag_router.register(r'documents', DocumentModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sample', include((sample_router.urls, 'myapp'), namespace='myapp')),    
    path('api/rag/', include((rag_router.urls, 'rag'), namespace='rag'))    
]
