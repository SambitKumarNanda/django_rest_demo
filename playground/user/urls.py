from django.urls import path
from user import views


urlpatterns = [
    path("dummy-api/", views.dummy_api, name="dummy-api"),
    path("dummy-rest-api/", views.DummyRestAPIView.as_view(), name="dummy_rest_api"),
    path("dummy-rest-api/<id>/", views.DummyRestAPIIDView.as_view(), name="dummy_rest_api"),
]
