from rest_framework_mongoengine import routers
from employeemanage.views import EmployeesView

router = routers.DefaultRouter()
router.register(r'employeemanage', EmployeesView)

urlpatterns = []
urlpatterns += router.urls