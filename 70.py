import requests

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}


url = "https://pythonhow.com/media/data/universe.txt"
response = requests.get(url,headers=headers)

print(response.status_code)
print(response.text)