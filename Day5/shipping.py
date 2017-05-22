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

    @classmethod
    def create_from_string(cls, string):
        cls.owner_code= string[1:2]
        #cls.category_id = string[3]
        cls.serial = string[4:-1]
        return cls(cls.owner_code, contents=None)


    #Constructor
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()
