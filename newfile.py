import re
import requests, json
import urllib.request
from datetime import timedelta
import datetime
toplam = 0

url = "https://api.c2me.cc/b/shuffle?region_code=34"

for a in range(99999999):
        a = requests.get(url).json()["online_users"]
        for i in range(len(a)):
        	toplam += len(a)
        	c = a[i]["created_at"]
        	c2 = ((c.split("."))[2])
        	if c2 == "2020":
                        kullanici = a[i]["nick"]
                        baglan = urllib.request.urlopen("https://connected2.me/"+ kullanici)
                        cıktı = baglan.read()
                        cıktı = cıktı.decode("utf-8")
                        r1 = re.findall(r"\b[0-9]{1,3}\b.dakika",cıktı)
                        r2 = ''.join(map(str, r1)).split()
                        dk = r2[0]
                        m = datetime.datetime.now() - datetime.timedelta(minutes=int(dk))
                        son = m.hour, '.', m.minute
                        values = ''.join(map(str, son))
                        va = float(values)
                    
                        if va <= 13.50 and va >=13.40:
                                wa = values,kullanici
                                print(wa)
                                print(wa, file=open("bulunan_hesaplar.txt","a"))
                                print("bakılan kişi sayısı",toplam)
