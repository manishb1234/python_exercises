import requests

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

url = "https://pythonhow.com/media/data/universe.txt"

response = requests.get(url, headers=headers)

content = response.text
count = 0
for i in content:
    if i == "a":
        count = count + 1

print(count)

"""
or text = response.text
count_a = text.count("a")
"""

#str class has count method


