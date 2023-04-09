import csv
import requests
import re
import time
urlbase="https://s.askci.com/stock/a/0-0?pageNum="
para={}
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
title=[]
data=[]
for i in range(1,252):
    url=urlbase+str(i)
    r=requests.get(url,params=para,headers=header)
    print(str(r.status_code)+": "+url)
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(r.text,"lxml")
    table=soup.find(id="myTable04")
    try:
        ths=table.find_all("th")
    except:
        print("failed")
        break
    title=[th.text for th in ths]
    tbody=table.find("tbody")
    trs=tbody.find_all("tr")
    for tr in trs:
        tds=tr.find_all("td")
        tdsv=[td.text for td in tds]
        data.append(tdsv)
    time.sleep(70)
print("writing to csv...")
f=open("output.csv","w",newline="")
writer=csv.writer(f)
writer.writerow(title)
for row in data:
    writer.writerow(row)
f.close()
print("done")


