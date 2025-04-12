#load content frm a link, multiply the content
#values by 2 and load the data into a new file

import requests
import csv

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

url = "https://pythonhow.com/data/sampledata.txt"

response = requests.get(url)
str_response = response.text
print(str_response)




#without csv
"""cleaned = str_response.replace("\n", ',')
parts = cleaned.split(',')
print("parts", parts)

lst=[]

for i in parts:
    if i.isdigit():
        lst.append(2*int(i))

    else:
        lst.append(i)

for i in range(0,len(lst), 2):
    lst.insert(i,'\n')
    #printint this
    # [6, 10, 8, 18, 12, 2, 0, 14, 2, 2, 16, 2, 4]

print(lst)



with open("73_file.txt",'w') as file:
    file.write"""