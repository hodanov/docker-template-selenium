from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


chrome_path = '/usr/bin/chromium-browser'
chromedriver_path = '/usr/lib/chromium/chromedriver'
o = Options()
o.binary_location = '/usr/bin/chromium-browser'
o.add_argument('--headless')
o.add_argument('--disable-gpu')
o.add_argument('--no-sandbox')
o.add_argument('--window-size=1200x600')

"""
Sample test
"""
d = webdriver.Chrome(chromedriver_path, options=o)
d.get('https://www.google.com')
print(d.title)
d.quit()

"""
Use the Chrome DriverService.
https://chromedriver.chromium.org/getting-started
"""
s = Service(executable_path=chromedriver_path)
s.start()
d = webdriver.Remote(
    s.service_url,
    desired_capabilities=o.to_capabilities()
)
d.get('https://www.google.com')
print(d.title)
d.quit()
