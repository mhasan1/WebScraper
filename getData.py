import requests
from lxml import html

url = 'https://www.investing.com/commodities/gold-historical-data'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)
#print(page.content)
tree = html.fromstring(page.content)


filename = "goldfile.csv"
goldfile = open(filename, "w")

for tr in tree.xpath('//*[@id="curr_table"]/tbody/tr'):
    goldDate = tr.xpath('td[1]/text()')
    goldPrice = tr.xpath('td[2]/text()')
    print('date: '+ goldDate[0], 'price: '+ goldPrice[0])
    #print('date: ', goldDate, 'price: ', goldPrice)
    #goldfile.write("Date: %s , price: %s\n" % (goldDate[0], goldPrice[0]))
    goldfile.write('%s:%s\n' % (goldDate[0], goldPrice[0]))

goldfile.close()
    