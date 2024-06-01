import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

Names = []
Prices = []
Disc = []
Reviews = []
for z in range(2, 5):

    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"+str(z)
    r = requests.get(url)
    print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="DOjaWF gdgoEp")
    names = box.find_all("div", class_="KzDlHZ")

    for i in names:
        n = i.text
        Names.append(n)
    print(len(Names))

    price = box.find_all("div", class_="Nx9bqj _4b5DiR")

    for b in price:
        p = b.text
        Prices.append(p)
    print(len(Prices))

    Descr = box.find_all("ul", class_="G4BRas")

    for c in Descr:
        d = c.text
        Disc.append(d)
    print(len(Disc))

    Rev = box.find_all("div", class_="XQDdHH")

    for t in Rev:
        sta = t.text
        Reviews.append(sta)
    print(len(Reviews))

df = pd.DataFrame({"Product Name": Names,"Price" : Prices, " Description": Disc, "Reviews": Reviews})
df.to_csv("E:\\coding\\Flipkart_Scraping.csv")

