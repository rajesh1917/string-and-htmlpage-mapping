from django.urls import include,path
from app2.views import *
app_name='something'

urlpatterns=[
    path('page1/',page1,name='page1'),
    ]