from django.conf.urls import url
from .views import ResponseForHome

urlpatterns = [
    url(r'^', ResponseForHome, name='home')
]