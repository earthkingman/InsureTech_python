import requests
from bs4 import BeautifulSoup as bs
URL = "http://www.naver.com"
res=requests.get(URL)
soup = bs(res.text)
# param = {"no":"1234","name":"Rekt77"}
# res = requests.get(URL,params=param)
for title in soup.find_all("strong",class_="title elss"):
    print(title.text)

