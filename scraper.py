import requests
from bs4 import BeautifulSoup
import smtplib
import re
import time

URL = 'https://www.amazon.com/346E2CUAE-Frameless-UltraWide-Adjustable-Replacement/dp/B08KFSMGJ8/ref=psdc_1292115011_t3_B08623SZH9'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", 'Cache-Control': 'no-cache', "Pragma": "no-cache"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find("span", class_='a-price-whole').get_text()
    fixed_price = float(re.findall(r'\d+.\d+', price)[0])

    print(title.strip())
    print(fixed_price)

    if(fixed_price < 600):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('kingmathers092@gmail.com', 'ixneuiijeyjezbca')

    subject = "Price fell down!"
    body = "Check the amazon link asap https://www.amazon.com/346E2CUAE-Frameless-UltraWide-Adjustable-Replacement/dp/B08KFSMGJ8/ref=psdc_1292115011_t3_B08623SZH9"

    msg = f"Subject: {subject}\n\n{body}"

    # don't use these emails, no need to hack ;)
    server.sendmail(
        'kingmathers092@gmail.com',
        'devstuff099@gmail.com',
        msg.encode('utf-8')
    )
    print("Email has been sent!")

    server.quit()

while True:
    check_price()
    time.sleep(60 * 60 *24)
