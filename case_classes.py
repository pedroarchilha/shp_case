import datetime
import pytz
from consolemenu import *
from consolemenu.items import *

_all_items = []


def _current_time():
    utc_time = datetime.datetime.utcnow()  #TODO: attirubte to sales list
    return pytz.utc.localize(utc_time)


class Items:
    """Simple class to create new items.

    Args:
        seller_name (str): The name of the seller.
        customer_name (str): The name of the customer for that item.
        sale_date (str): The date the sale was made.
        sale_item_name (str): The name of the item.
        sale_value (int): The value of the respective sale.
    """

    def __init__(self, seller_name, customer_name, sale_date,
                 sale_item_name, sale_value):

        self._seller_name = seller_name
        self.customer_name = customer_name
        self.sale_date = sale_date
        self.sale_item_name = sale_item_name
        self.sale_value = sale_value


class Seller:
    """Basic class to store seller information.

    Attributes:
        name (str): The name of the artist.
        items_list (list[items]): A list containing items registered
            by the seller.

    Methods:
        add_item: used to add a registered item.
    """

    def __init__(self, name):
        self.name = name
        self.items_list = []

    def add_item(self, name):
        """Simple function to add created items to a main list for future
            consult.
        """
        item_found = find_object(name, self.items_list and _all_items)  #TODO: append an Items object.
        if item_found is not None:
            self.items_list.append(item_found)
            _all_items.append(item_found)
        else:
            print("Item already exists.")


def find_object(item, object_list):
    """Check `object_list`  to see if an object with a name attribute
        equal to `item`  exists, return it if so. Otherwise, `the item`
        will not be created.
    """
    for item in object_list:
        if item.name == item:
            return None
    return item


# TODO create a method for new Seller registration


def main_menu():
    print("[1] Seller Options")
    print("[2] Customer Options")
    print("[3] Sales Options")

    option = ""
    if option == "1":
        seller_options()
    elif option == "2":
        customer_options()


def seller_options():
    print("[1] Register new product")
    print("[2] Register new sale")
    print("[3] Remove item")
    print("[4] Main menu")

    option = ""
    if option == "4":
        main_menu()


def customer_options():
    print("[1] Register new customer")
    print("[2] Remove customer")
    print("[3] Main Menu")

    option = ""
    if option == "3":
        main_menu()
