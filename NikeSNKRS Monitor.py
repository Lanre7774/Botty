
import requests
import time
import json
from bs4 import BeautifulSoup
import threading
import randomheaders

def monitor():
    source = requests.get('https://www.nike.com/launch/', headers=randomheaders.LoadHeader()).text
    soup = BeautifulSoup(source, 'lxml')
    webhook = 'https://discord.com/api/webhooks/910030730845892638/r8_FkWqwwe02thaV7SbWOBjWyKwtjba_C_cgGcT8DkVdWb2DHqWDUkN-hZYePc5iEer-'
    for hrefs in soup.find_all('figure', class_='pb2-sm va-sm-t ncss-col-sm-12 ncss-col-md-6 ncss-col-lg-4 pb4-md prl0-sm prl2-md ncss-col-sm-6 ncss-col-lg-3 pb4-md prl2-md pl0-md pr1-md'):
        url = "https://www.nike.com" + hrefs.a.get('href')
        filename = 'nikelinks.txt'
        with open(filename, 'r')as rf:
            with open(filename, 'a') as af:
                read = rf.read()
                if url not in read:
                    print(url)
                    af.write('\n' + url)
                    data = {

                        "username": "Botty",
                        "content": url               
                    }
                    requests.post(webhook, data=data)
                else:
                    print("No new links")

    time.sleep(60)

while True:
    monitor()