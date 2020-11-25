from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Accounts,Department,Product,Opportunities,Contacts,Service
from rest_framework import viewsets, permissions
from .serializers import ContactsSerializer, AccountsSerializer, DepartmentSerializer,ServiceSerializer,OpportunitiesSerializer
from .serializers import ProductSerializer
import json
import math

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

class ContactsView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OpportunitiesView(viewsets.ModelViewSet):
    queryset = Opportunities.objects.all()
    serializer_class = OpportunitiesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET', 'POST', 'DELETE'])
def accounts_list(request):
    if request.method == 'GET':
        accounts_full = Accounts.objects.all()
        accounts = get_accounts_by_filter(request,accounts_full)
        accounts_serializer = AccountsSerializer(accounts, many=True)
        return JsonResponse(accounts_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    account_name = request.GET.get('account_name', None)
    if account_name is not None:
        return JsonResponse({'message': '{} Accounts were deleted successfully!'.format(account_name)},
                        status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        account_data = JSONParser().parse(request)
        accounts_serializer =  AccountsSerializer(data=account_data)
        #Check if we have this account , if not we enable the save of new account
        account = accounts_serializer.Meta.model
        if check_not_exsiting_account(account):
            if accounts_serializer.is_valid():
                accounts_serializer.save()
                return JsonResponse(accounts_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(accounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'Accounts with name {0} already exits!'.format(account.account_name)},
                                status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        accounts_full = Accounts.objects.all()
        account_data = JSONParser().parse(request)
        # Check if we have this account , if not we enable the save of new account
        acount_id = account_data['acount_id']
        contacts_l = account_data['contacts']
        count = 0
        for account in accounts_full:
            if acount_id == account.acount_id:
                #Delete all contact that were connected to account
                for c in contacts_l:
                    contact = Contacts.objects.filter(id=c)
                    contact.delete()
                count += account.delete()
        return JsonResponse({'message': '{} Accounts were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
###
# We check if the account is in the data base, if exist return false else true
# so
# ###
def check_not_exsiting_account(account):
        account_name = account.account_name
        list = Accounts.objects.filter(account_name__icontains=account_name)
        if len(list) == 0:
            return True
        return False
###
# This method is for select account by account name like 'Bezek internetional'
# ###
@csrf_exempt
def AccountView(request,nm):
    try:
        account = Accounts.objects.get(id = nm)
    except Accounts.DoesNotExist:
        return JsonResponse({'message': 'The Accounts does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        account_serializer = AccountsSerializer(account)
        return JsonResponse(account_serializer.data)

    elif request.method == 'PUT':
        account_data = JSONParser().parse(request)
        account_serializer = AccountsSerializer(account, data=account_data)
        #Check if we have this account , if not we enable the save of new account
        account = account_serializer.Meta.model
        if check_not_exsiting_account(account):
            if account_serializer.is_valid():
                account_serializer.save()
                return JsonResponse(account_serializer.data)
            return JsonResponse(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'Accounts with name {0} already exits!'.format(account.account_name)},
                                status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        contacts = []
        contacts = account.contacts
        #delete all contacts of this account
        for c in contacts:
            contact = Contacts.objects.filter(id__icontains=c)
            contact.delete()
        account.delete()

        return JsonResponse({'message': 'Account was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



###
# Get the account list by filter
# if we add to the post the data ?id=3 or ?acount_id=5001 or ?account_name=Home
# we will get the list by the filter
# ###
def get_accounts_by_filter(request,accounts_f):
    # Get filter by id - if we send the command http://127.0.0.1:8000/accounts/?id=3
    id = request.GET.get('id', None)
    if id is not None:
        accounts = accounts_f.filter(id__icontains=id)
    else:
        # Get filter by account_id - if we send the command http://127.0.0.1:8000/accounts/?acount_id=5001
        acount_id = request.GET.get('acount_id', None)
        if acount_id is not None:
            accounts = []
            for account in accounts_f:
                if account.acount_id == acount_id:
                    accounts.append(account)
        else:
            # Get filter by account_name - if we send the command http://127.0.0.1:8000/accounts/?account_name=Home
            account_name = request.GET.get('account_name', None)
            if account_name is not None:
                accounts = []
                for account in accounts_f:
                    if account.account_name == account_name:
                        accounts.append(account)
            else:
                accounts = accounts_f
    return accounts
