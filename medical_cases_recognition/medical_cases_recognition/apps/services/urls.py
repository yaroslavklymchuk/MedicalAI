from django.conf.urls import url
from .views import ResponseForServices

urlpatterns = [
    url(r'^', ResponseForServices, name='services')
]