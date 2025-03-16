from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

try:
    jsondata = {}
    data = dict()
    url = "https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+page+site+area/bugun"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

    webdriver = webdriver.Chrome(options=options)
    webdriver.get(url)

    webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    soup = BeautifulSoup(webdriver.page_source,"html.parser")
    table =soup.find("table",class_="kurlarTablo")
    tbody = table.find("tbody")
    trs=tbody.find_all("tr")
    for tr in trs:
        tds=tr.find_all("td")
        paraadi=tds[2]
        parabirim=tds[1]
        alis = tds[3]
        satis=tds[4]
        efalis=tds[5]
        efsatis = tds[6]
        data = {
            paraadi.text:{
                "birim":parabirim.text,
                "alış":alis.text,
                "satış":satis.text,
                "efektif alış":efalis.text,
                "efektif satış":efsatis.text
            }
        }
        jsondata.update(data)
        data={}
except WebDriverException:
    print("web driver bulunamadı indirmek istermisin? (y/n)")
    result = input().lower()
    if result == "n":
        pass
    else:
        from downloadwebdriver import downloaddrivers
        import webbrowser
        downloaddrivers()
        print("Drivers downloaded")
        print("follow this steps")
        webbrowser.open("https://youtu.be/dz59GsdvUF8?si=U-O7csT6D08FCGyy")

        



