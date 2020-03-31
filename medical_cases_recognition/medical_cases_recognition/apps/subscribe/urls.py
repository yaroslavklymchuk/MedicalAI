from django.conf.urls import url
from .views import ResponseForSubscribe

urlpatterns = [
    url(r'^', ResponseForSubscribe, name='subscribe')
]