#http://www.imdb.com/chart/top?ref_=nv_mv_250_6

def __str__(self): #bir classın bir dict objesi olarak çağırdığınızda string olarak çıktısnı veriyor.

import requests
from bs4 import BeautifulSoup
html_data=requests.get("http://www.imdb.com/chart/top?ref_=nv_mv_250_6").content
soup_data=BeautifulSoup(html_data,"html.parser") #parserlere ayırmak için.
tbody_data=soup_data.find("tbody",{"class":"lister-list"}) #unique bir class seçmemiz gerektiği için tbody classını kopyaladık.soup data ile objenin direk kendisini gönderirdi ama printleseydik string oalrak gönderdi.
for tr_data in tbody_data.find_all("tr"):
    isim_td=tr_data.find("td",{"class":"titleColumn"})
    rating_td=tr_data.find("td",{"class":"ratingColumn"})
    print(isim_td.find("a")["href"]) #bir parametreden veri almak istediğimizde dict olarak almak istediğimizde [] böyle yazıyoruz
    print(isim_td.find("a").text,rating_td.find("strong").text)
