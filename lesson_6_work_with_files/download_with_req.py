import requests
import os

url = 'https://www.selenium.dev/images/sponsors/browserstack.png'
response = requests.get(url=url)
content = response.content

with open('resources/selenium_img.png', 'wb') as file:
    file.write(content)

size = os.path.getsize('resources/selenium_img.png')
assert size == 23783

