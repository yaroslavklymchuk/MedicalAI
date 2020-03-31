from django.conf.urls import url
from .views import ResponseForDetection
from ..subscribe.views import ResponseForSubscribe

urlpatterns = [
    url(r'^', ResponseForDetection, name='detection'),
    url(r'subscribe/', ResponseForSubscribe, name='subscribe')
]