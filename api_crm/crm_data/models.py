from django.db import models

###
# Hold the list of Products in the organization
#
# ###
class Product(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return  str(self.product_id) + ' - ' +self.name
###
# Hold the list of Services in the organization
#
# ###
class Service(models.Model):
    service_id = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return  str(self.service_id) + ' - ' +self.name

###
# Hold the list of departments in the organization
#
# ###
class Department(models.Model):
    department_id = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return  str(self.department_id) + ' - ' +self.name
###
# Hold the list of Contacts people in the organization
#
# ###
class Contacts(models.Model):
    contact_id = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    fax_number = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.contact_id) + ' - ' + self.first_name + ' ' +self.last_name
###
# Hold the list of Accounts list
#
# ###
class Accounts(models.Model):
    acount_id = models.IntegerField()
    account_name = models.CharField(max_length=250)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    contacts = models.ManyToManyField(Contacts)

    def __str__(self):
        return str(self.acount_id) + ' - ' +self.account_name



###
# Hold the list of Opportunities list
#
# ###
class Opportunities(models.Model):
    opportunity_id = models.IntegerField()
    name = models.CharField(max_length=50)
    acount_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    services = models.ManyToManyField(Service)
    def __str__(self):
        return str(self.opportunity_id) + ' - ' +self.name

