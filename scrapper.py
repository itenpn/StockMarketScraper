from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

stock_name = input("Please list a ticker ")
page_url = 'https://finance.yahoo.com/quote/' + stock_name + '?p=' + stock_name

for i in range(50):
    page = urlopen(page_url)
    soup = BeautifulSoup(page, 'html.parser')

    name_data = soup.body.find('h1', attrs={'data-reactid':'7'})
    name = name_data.text

    beta_data = soup.body.find('span', attrs={'data-reactid':'61'})
    beta = beta_data.text

    PE_data = soup.body.find('span', attrs={'data-reactid':'66'})
    PE_Ratio = PE_data.text

    EPS_data = soup.body.find('span', attrs={'data-reactid':'71'})
    EPS = EPS_data.text

    price_data = soup.body.find('span', attrs={'data-reactid':'14'})
    price = price_data.text

    print(name)
    print('Price: ' + price)
    print('Beta: ' + beta)
    print('PE Ratio: ' + PE_Ratio)
    print('EPS: ' + EPS)
    time.sleep(5)
