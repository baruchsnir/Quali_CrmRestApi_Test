import requests
import json

###
# Get Accounts from Rest Api
# ###
def get_accounts(filter):
    filter_s = str(filter)
    headers = {
        'Authorization': 'Basic YmFydWNoOkJzNTUwODE3OQ==',
        'Content-Type': 'application/json'
    }
    jobs = []
    payload = {}
    current_temp = 0.0
    url = 'http://127.0.0.1:8000/accounts/'
    if filter_s != '':
        if type(filter) == int:
            url = url + filter_s + "/"
        else:
            if '=' in filter_s:
                url = url +"?"+ filter_s

    #Get the json data from Rest IP
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text.encode('utf8'))
    return data

def get_contacts(filter):
    headers = {
        'Authorization': 'Basic YmFydWNoOkJzNTUwODE3OQ==',
        'Content-Type': 'application/json'
    }
    jobs = []
    payload = {}
    current_temp = 0.0
    url = 'http://127.0.0.1:8000/contacts/'
    if filter != '':
        url = url +filter +"/"
    #Get the json data from Rest IP
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text.encode('utf8'))
    return data
def add_contact(payload):

    url = "http://127.0.0.1:8000/contacts/"

    headers = {
        'Authorization': 'Basic YmFydWNoOkJzNTUwODE3OQ==',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
    data = json.loads(response.text.encode('utf8'))
    id = data['id']
    return id
def delete_contact(payload):

    url = "http://127.0.0.1:8000/contacts/"

    headers = {
        'Authorization': 'Basic YmFydWNoOkJzNTUwODE3OQ==',
        'Content-Type': 'application/json'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))

def add_account(data):
    url = "http://127.0.0.1:8000/accounts/"

    payload = data
    headers = {
        'Authorization': 'Basic YmFydWNoOkJzNTUwODE3OQ==',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
    data = json.loads(response.text.encode('utf8'))
    id = data['id']
    return id
def delete_account(data):
    url = "http://127.0.0.1:8000/accounts/"

    payload = data
    headers = {
        'Authorization': 'Basic YmFydWNoOkJzNTUwODE3OQ==',
        'Content-Type': 'application/json'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
print('--------------------------')
print('Full Accounts')
accounts = get_accounts("")
print(accounts)
print('--------------------------')
filter = 'id=2'
print('Accounts with filter',filter)
accounts = get_accounts(filter)
print(accounts)
print('--------------------------')
filter = 'acount_id=5003'
print('Accounts with filter',filter)
accounts = get_accounts(filter)
print(accounts)

print('--------------------------')
print('Full Contacts')
contacts = get_contacts("")
print(contacts)
print('--------------------------')
filter = '3 '
print('Contacts with filter',filter)
contacts = get_contacts(filter)
print(contacts)
print('------------------------------------------------------------------------------')
print('delet contact')
data = {
    "id": 5,
    "contact_id": 3011,
    "first_name": "Yosi",
    "last_name": "Avraham",
    "country": "usa",
    "city": "la",
    "address": "marina 5",
    "phone_number": "0502345678",
    "fax_number": "0502345679",
    "department": 4,
    "age": 33,
    "email": "yavraham@walla.com",
    "url": "http://127.0.0.1:8000/contacts/5/"
}
delete_contact(json.dumps(data))
print('Add contact')
data = {
    "contact_id": 3011,
    "first_name": "Yosi",
    "last_name": "Avraham",
    "country": "usa",
    "city": "la",
    "address": "marina 5",
    "phone_number": "0502345678",
    "fax_number": "0502345679",
    "department": 4,
    "age": 33,
    "email": "yavraham@walla.com"
}
# payload = "{\n    \"contact_id\": 3011,\n    \"first_name\": \"Yosi\",\n    \"last_name\": \"Avraham\",\n    \"country\": \"usa\",\n    \"city\": \"la\",\n    \"address\": \"marina 5\",\n    \"phone_number\": \"0502345678\",\n    \"fax_number\": \"0502345679\",\n    \"department\": 4,\n    \"age\": 33,\n    \"email\": \"yavraham@walla.com\"\n}"

contact_id = add_contact(json.dumps(data))
print('Add Account')
data = {
        "id": 1,
        "acount_id": 5007,
        "account_name": "Orad",
        "country": "Israel",
        "city": "Holon",
        "address": "hamlach 39",
        "phone_number": "035660000",
        "email": "orad@hotmail.com",
        "contacts": [contact_id,]
    }
id = add_account(json.dumps(data))
filter = 'acount_id=5007'
print('Accounts with filter',id)
accounts = get_accounts(id)
print(accounts)
print('------------------------------------------------------------------------------')
print('Delet Contact')
if len(accounts) > 0:
    data = {
        "id": id,
        "acount_id": 5007,
        "account_name": "Orad",
        "country": "Israel",
        "city": "Holon",
        "address": "hamlach 39",
        "phone_number": "035660000",
        "email": "orad@hotmail.com",
        "contacts": [contact_id,]
    }
    delete_account((json.dumps(data)))
