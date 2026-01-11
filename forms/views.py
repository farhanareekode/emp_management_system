from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FormField

# Create your views here.
@api_view(['GET'])
def get_form_schema(request):
    fields = FormField.objects.order_by("order").values(
        "id", "label", "field_type", "required"
    )
    return Response({"fields": list(fields)})
@api_view(['POST'])
def update_form_schema(request):
    FormField.objects.all().delete()

    for index, field in enumerate(request.data["fields"]):
        FormField.objects.create(
            label=field["label"],
            field_type=field["field_type"],
            required=field.get("required", False),
            order=index
        )

    return Response({"status": "form updated"})
