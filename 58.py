#add a new employee to dictionary in
#json file

import json
from pprint import pprint

with open("misc/57_company1.json", 'r+') as file:
    d = json.loads(file.read())
    pprint(d)
    d['employees'].append(dict(firstName="Albert",
                               lastName="Bert"))
    pprint(d)
    file.seek(0)
    json.dump(d, file, indent = 4, sort_keys=True)
    file.truncate()

