from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee

@api_view(['GET', 'POST'])
def employees_view(request):
    if request.method == 'GET':
        employees = Employee.objects.all().values("id", "form_data")
        return Response(list(employees))

    if request.method == 'POST':
        Employee.objects.create(form_data=request.data["form_data"])
        return Response({"status": "created"})


@api_view(['GET'])
def get_employee(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    return Response({"id": emp.id, "form_data": emp.form_data})


@api_view(['PUT'])
def update_employee(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    emp.form_data = request.data["form_data"]
    emp.save()
    return Response({"status": "updated"})


@api_view(['DELETE'])
def delete_employee(request, emp_id):
    Employee.objects.filter(id=emp_id).delete()
    return Response({"status": "deleted"})
