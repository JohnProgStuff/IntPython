import iso6346

class ShippingContainer:
    next_serial = 1337


    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial +=1
        return result

    #Constructor
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None) #We don't know the contents yet

    #Constructor
    @classmethod
    def create_with_items(cls, owner_code, *items): #this makes the above constructor obsolete
    #def create_with_items(cls, owner_code, items): #this requires a list ("books","clothes") to be given
        #return cls(owner_code, contents=list(items)) #instructors way
        return cls(owner_code, contents=list(items)) #without list() it will return a tuple

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    #Constructor
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        #self.serial = ShippingContainer._get_next_serial()
        self.bic = ShippingContainer._make_bic_code(owner_code=owner_code, serial=ShippingContainer._get_next_serial())