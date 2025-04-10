import json
from pprint import pprint

with open("misc/57_company1.json") as file:
        #class str
        output = file.read()
        #create a dict of output
        a = json.loads(output)


print(a)
pprint(a)