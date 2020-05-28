import requests
from bs4 import BeautifulSoup
import re

def get_html_urls():
    url = "https://www.5442tu.com/mingxing/"
    # url = "https://www.5442tu.com/mingxingtuku/"
    r =requests.get(url)
    r.encoding='gb2312'
    soup =BeautifulSoup(r.text,"html.parser")
    links = soup.find_all("a",href =re.compile(r"//www.5442tu.com/mingxing/\d+/\d+.html"))
    # links = soup.find_all("a",href =re.compile(r"//www.5442tu.com/mingxingtuku/\d+/\d+.html"))

    urls=[]
    for link in links:
        urls.append(link['href'])
    return urls

def craw_html(fname,url):
    r = requests.get(url)
    r.encoding = 'gb2312'
    soup =BeautifulSoup(r.text,"html.parser")
    img_url =soup.find("div",class_="arcBody").find("p").find("img").get("src")
    download_img(fname,img_url)

def download_img(fname,img_url):
    headers = {
        "Referer":"https://www.5442tu.com/mingxing/20200520/108768.html",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    r=requests.get(img_url,headers=headers)
    with open("%s.jpg"%fname,"wb") as fout:
        fout.write(r.content)
idx=80
for url in get_html_urls():
    idx+=1
    print(url)
    craw_html(str(idx),url)
