from lxml import html
import requests
import os
import time

while True:
    page = requests.get("http://www.walmart.com/ip/46189328")
    tree = html.fromstring(page.text)
    availability = tree.xpath('//*[@id="WMNotAvailableLine"]/span/text()')

    if availability != ['Not Available at this time']:
        os.system("""osascript -e 'display notification "Amiibos In Stock @ Walmart" with title "GOGOGO"'""")
        os.system("afplay /Users/JarvisHax/Desktop/Amiibo/amiibo.mp3")
    time.sleep(60)
