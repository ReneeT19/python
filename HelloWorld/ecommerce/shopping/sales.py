# absolute import is the best practice unless it's too complicated
# from ecommerce.customer import contact
# # or use relative import:
# # from ..customer import contact
# contact.contact_customer()
# every module has a built-in method to print the name of the module
print("Sales initialized", __name__)


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":
    print("Sales started")
    calc_tax()
