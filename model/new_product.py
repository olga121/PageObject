from sys import maxsize

class New_product:
    def __init__(self, name=None,  code=None, quantity=None, date_valid_from = None, date_valid_to = None,
                 manufacturer = None, keywords=None, price = None):
        self.name = name
        self.code =code
        self.quantity = quantity
        self.date_valid_from = date_valid_from
        self.date_valid_to = date_valid_to
        self.manufacturer = manufacturer
        self.keywords = keywords
        self.price = price

    def __repr__(self):
        return "%s:%s" % (self.code, self.name)

    def __eq__(self, other):
        return (self.code is None or other.code is None or self.code == other.code) and self.name == other.name

    def id_or_max(self):
        if self.code:
            return int(self.code)
        else:
            return maxsize