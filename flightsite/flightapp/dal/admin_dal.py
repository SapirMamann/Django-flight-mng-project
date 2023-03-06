from flightapp.models import Customer
"""
Module that interacts with MySql database,
CRUD 
"""
class Admin():
    def get_all_customers():
        cust_list =  Customer.objects.all()
        return cust_list
    
    def get_cust_by_id():
        pass
    