from django.urls import path
from .views import test_hello_name

urlpatterns = [
    path("test-hello-name/<name>/", test_hello_name, name="test_hello_name")
]
