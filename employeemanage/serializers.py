from employeemanage.models import Employee
from rest_framework_mongoengine import serializers


class EmployeeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Employee
        fields = "__all__"