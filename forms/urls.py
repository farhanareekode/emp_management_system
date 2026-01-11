from django.urls import path
from .views import get_form_schema, update_form_schema

urlpatterns = [
    path("form-schema/", get_form_schema),
    path("form-schema/update/", update_form_schema),
]
