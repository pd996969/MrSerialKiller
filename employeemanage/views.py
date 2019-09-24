from rest_framework_mongoengine import viewsets as meviewsets

from employeemanage.models import Employee
from employeemanage.serializers import EmployeeSerializer


class EmployeesView(meviewsets.ModelViewSet):
    lookup_field = 'empId'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer