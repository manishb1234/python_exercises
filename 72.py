#Create a script that let the user type in a search term and opens and
#search on the browser for that term on Google

import webbrowser

user_input = input("Enter a search term: ")

url=f"https://www.google.com/search?q={user_input}"
#webbrowser.open("https://www.google.com/search?q=%s" % user_input)

webbrowser.open_new_tab(url)