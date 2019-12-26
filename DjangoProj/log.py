import requests
from bs4 import BeautifulSoup
import time
import lxml

def update():
    login_data = {
        'uname': 'M24',
        'pwd': 'P24',
        'op': 'Login'
    }
    with requests.Session() as s:
        url = 'https://projectdivesy.000webhostapp.com/sqldata2.php'
        r = s.get(url)
        time.sleep(2)
        soup = BeautifulSoup(r.text, 'lxml')
        time.sleep(2)
        r = s.post(url, data=login_data)

    #print stuff
    soup=BeautifulSoup(r.text, 'lxml')
    defination=soup.find_all('p')
    for i in defination:
        stringl=len(i.string)
        #print(i.string[2:stringl-1])
        print(i.string[2:])

    changeUrl= 'https://projectdivesy.000webhostapp.com/change1.php'
    time.sleep(2)
    rc = s.post(changeUrl, data=login_data)
    print("processing...")
    time.sleep(5)
    print("done")

update()
