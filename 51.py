print(type("Hey".replace("ey","i")[-1]))

#replace method returns a string

import shutil
import os



source=r"F:\Python Exercises\textfiles\51.py"

destination = r"F:\Python Exercises\51.py"

if not os.path.exists(destination):
    shutil.move(source, destination)
else:
    print("File already exists")