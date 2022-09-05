from consolemenu import *
from consolemenu.items import *
import case_classes


menu = ConsoleMenu("Company App", "Please, select an option")

seller_options = SelectionMenu("register_new_seller", "register created item",
                               "func_register_new_customer")  #TODO Seller("new_seller")
item_options = SelectionMenu("class_create_new_item")  # create new class and func to attribute - OK
sales_options = FunctionItem("Call ")

seller_menu = SubmenuItem("Seller options", seller_options, menu)
item_menu = SubmenuItem("Item options", item_options, menu)
sales_menu = SubmenuItem("Sales options", sales_options, menu)

menu.append_item(seller_menu)
menu.append_item(item_menu)

menu.show()

# help(ConsoleMenu)
