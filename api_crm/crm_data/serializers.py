from rest_framework import serializers
from .models import Accounts,Department,Product,Opportunities,Contacts,Service


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['id',"acount_id", "account_name", "country", "city", "address", "phone_number", "email", "contacts"]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id',"department_id", "url", "name"]


class OpportunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunities
        fields = ['id',"opportunity_id","name", "url","url","url"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id',"product_id",  "name"]

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id',"service_id", "name"]

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id',"contact_id", "first_name","last_name","country","city","address","phone_number","fax_number","department"
            ,"age","email","url"]
