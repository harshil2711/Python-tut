import multiprocessing
import requests

url = "https://images.unsplash.com/photo-1661261656149-879b82aaad59?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
def downloadfile(url , name):
    r = requests.get(url)
    open(f'D:/Me/Python-tut-main/images/{i}.jpg', 'wb').write(r.content)



for i in range(5):
    downloadfile(url , i)
