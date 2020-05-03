import requests

url= "http://155.41.7.243:8888/?id=Logan%20Airport"
r = requests.get(url)

print (type(r))