# GET request
import requests

r = requests.get("https://www.spinny.com/")
print(r.text)

# _________________________________________________________________________
# POST request

import requests
d = {"name":"tom", "job":"Dev"}
r = requests.post("https://reqres.in/api/users" ,d )

print(r.text)

# Output
# {"name":"tom","job":"Dev","id":"144","createdAt":"2023-03-11T19:47:02.369Z"}

# ______________________________________________________________________
# To see all the h2 tags on the page.

import requests
import bs4

r = requests.get("https://www.spinny.com/")
b = bs4.BeautifulSoup(r.text , 'html.parser')

# print(b.prettify())

for tags in b.findAll("h2"):
    print(tags.text)