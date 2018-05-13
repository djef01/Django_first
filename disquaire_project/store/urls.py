from django.conf.urls import url

from . import views # Import views so we can use them in urlsself.

urlpatterns = [
    url('', views.listing),
]
