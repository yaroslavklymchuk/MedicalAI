from django.conf.urls import url
from .views import ResponseForDetection

urlpatterns = [
    url(r'^', ResponseForDetection, name='detection')
]