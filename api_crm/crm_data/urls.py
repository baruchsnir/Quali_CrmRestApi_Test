from django.contrib import admin
from django.urls import path,include,utils
from django.conf.urls import url
from . import views
# from . import models
from rest_framework import routers
router = routers.DefaultRouter()
# router.register('accounts',views.AccountsView)
router.register('contacts',views.ContactsView)
router.register('departments',views.DepartmentView)
router.register('opportunities',views.OpportunitiesView)
router.register('service',views.ServiceView)
router.register('product',views.ProductView)


urlpatterns = [
   path('',include(router.urls)),
   path('accounts/', views.accounts_list),
   path('accounts/<int:nm>/',views.AccountView),
]
