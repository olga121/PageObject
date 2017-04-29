from model.new_product import New_product
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of products","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/products.json"

for o, a in opts:
    if o =="-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_letters(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_numbers(prefix, maxlen):
    symbols = string.digits + "-"*3 + " "*3
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [New_product(name="", code="", quantity="", date_valid_from = "", date_valid_to = "",
                    manufacturer = "", keywords="", price = "")] + [
    New_product(name=random_string_letters("name", 10), code = random_string_numbers("code", 10),
                quantity = random_string_numbers("quantity", 10), keywords=random_string_letters("keywords", 20),
                date_valid_from = random_string_numbers("date_valid_from", 20), date_valid_to = random_string_numbers("date_valid_to", 10),
                manufacturer=random_string_letters("manufacturer", 20), price = random_string_numbers("price", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))