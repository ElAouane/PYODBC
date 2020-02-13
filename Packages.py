import requests


web_page = requests.get('http://www.perdu.com')

print(web_page)
print(type(web_page))

print(web_page.cookies)