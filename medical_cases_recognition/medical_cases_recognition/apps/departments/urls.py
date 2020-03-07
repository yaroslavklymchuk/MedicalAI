from django.conf.urls import url
from .views import ResponseForDepartments

urlpatterns = [
    url(r'^', ResponseForDepartments, name='departments')
]