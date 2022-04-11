import requests
from requests import Session
from bs4 import BeautifulSoup as bs
from pprint import pprint
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# PhantomJSをSelenium経由で利用します.
driver = webdriver.PhantomJS()



exit()

email = "mine.mail.444@gmail.com"
password = "Atam1526"

URL = 'https://bible.prsi.org/ja/'
LOGIN_ROUTE = 'Account/Login'


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'origin': URL, 
    'referer': URL + LOGIN_ROUTE
    }


s = requests.session()
# token = s.get(URL).cookies['__RequestVerificationToken']
site = s.get(URL)
bs_content = bs(site.content, "html.parser")
token = bs_content.find("input", {"name":"__RequestVerificationToken"})["value"]
login_payload = {
        'Email': email,
        'Password': password,
        '__RequestVerificationToken': token
        }

login_req = s.post(URL + LOGIN_ROUTE, headers=HEADERS, data=login_payload)
print(login_req.status_code)
cookies = login_req.cookies

soup = bs(s.get(URL+"Player").content, "html.parser")

# title = soup.select("#location_book")

# data = requests.get(URL+"Player").json()
title = soup.find("div", {"id": "bible_name"})

print(title)

s.close()
# url = "https://bible.prsi.org/ja/Player"


# with Session() as s:
#     site = s.get(url)
#     bs_content = bs(site.content, "html.parser")
#     token = bs_content.find("input", {"name":"__RequestVerificationToken"})["value"]
#     login_data = {"username":email, "password":password, "__RequestVerificationToken":token}
#     s.post(url, login_data)


#     site = s.get(url)

#     print(site.content)

#     # home_page = s.get("https://bible.prsi.org/ja/Player")

#     soup = bs(site.content, 'html.parser')
#     title = soup.find('title')
#     # book = soup.select("#bible_name")
#     print(title)


#     "https://bible.prsi.org/ja/Account/Login"


#     '''
#     User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36

#     TOKEN: __RequestVerificationToken
#     '''