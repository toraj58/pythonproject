class Product:

    # Class Attribute
    type = 'parcel'

    # Initializer / Instance Attributes
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def printproduct(self):
        print('Product Name : ', self.name)