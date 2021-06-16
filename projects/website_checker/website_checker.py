from bs4 import BeautifulSoup
import requests
import sys
from colorama import Fore


try:
    def find(url):
        req=requests.get(url)
        response_text=req.text
        soup = BeautifulSoup(response_text, 'html.parser')
        list=[href.get('href') for href in soup.find_all('a')]
        for i in list:
            new=url+i
            resp=requests.get(new)
            if(resp.status_code==200):
                print(Fore.GREEN+f'{resp.status_code}------>{new}')
            else:
                print(Fore.BLUE + f'{resp.status_code}------>{new}')
    
    print("Enter a port or range of ports in format(1-10)")
    ports=[int(i) for i in input().split("-")]
    url=input('Enter The url : ')
    while('http://' not in url and 'https://' not in url ):
        print("Enter correct Url")
        url=input('Enter The url : ')
    if(len(ports)>1 and ports[0]>ports[1]):
        for port in ports:
            resp=requests.get('{}:{}'.format(url,str(port)))
            print(resp.status_code)
    else:
        resp=requests.get('{}:{}'.format(url,str(ports)))
    print("Status code",resp.status_code)
    print("You can check the following properties of the respose\n1>apparent_encoding\n2>close\n3>connection\n4>content\n5>cookies\n6>elasped\n7>encoding\n8>headers\n9>history\n10>raw\n11>reason\n12>request\n13>status_code\n14>text\n15>url\n16>Spidering\npress q to quit()")
    while(True):
        print("Enter the property")
        prop=input().strip()
        if(prop=="apparent_encoding"):
            print(resp.apparent_encoding)
        if(prop=="close"):
            print(resp.close)
        if(prop=="connection"):
            print(resp.connection)
        if(prop=="content"):
            print(resp.content)
        if(prop=="cookies"):
            print(resp.cookies)
        if(prop=="elasped"):
            print(resp.elasped)
        if(prop=="encoding"):
            print(resp.encoding)
        if(prop=="headers"):
            print(resp.headers)
        if(prop=="history"):
            print(resp.history)
        if(prop=="raw"):
            print(resp.raw)
        if(prop=="reason"):
            print(resp.reason)
        if(prop=="status_code"):
            print(resp.status_code)
        if(prop=="text"):
            print(resp.text)
        if(prop=="url"):
            print(resp.url)
        if(prop=="Spidering"):
            find(url)
        if(prop=="q"):
            print("Thank You")
            resp.close
            quit()
except KeyboardInterrupt:
    print("\nsession Terminated")
    quit()