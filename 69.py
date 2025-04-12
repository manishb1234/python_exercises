import requests

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers=headers)
print(r.text[:100])

print(__name__)

#error: earlier this file was
# requests(same name as library), thus error

"""Expected Output
<!DOCTYPE html>
<!--[if IE 7]>
<html class="ie ie7" 
lang="en-US" prefix="og: http://ogp.me/ns#">
"""

"""In the code, Python is actually 
referring to the script name, 
which is requests  And it doesn't find a 
get attribute for that name. 
Script names load in the current namespace. 
They are actually stored in the __name__ 
variable. You could try to print that
variable out, and you would see that
it prints your script name.
Therefore you should not name 
your scripts under library names. """