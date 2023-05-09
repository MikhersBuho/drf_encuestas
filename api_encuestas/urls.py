from django.urls import path
from rest_framework import routers

from .views import UserList, CompanyList, DomainList

router = routers.DefaultRouter()
router.register('user', UserList, 'user')
router.register('company', CompanyList, 'company')
router.register('domain', DomainList, 'domain')

urlpatterns = router.urls

# urlpatterns = [
#     path('user/', UserList.as_view(), name='user-list'),
# ]
