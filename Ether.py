import urllib3
import time
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
while(1) :
    time.sleep(5)
    response = http.request('GET', 'https://www.coingecko.com/en/coins/ethereum')
    eth_string = BeautifulSoup(response.data,features="lxml")  # Note the use of the .data property
    eth_string=str(eth_string)
    eth_string=eth_string[eth_string.find('{"@type":"Offer","price":"'):eth_string.find('","priceCurrency":"USD"}}')]
    eth_string=float(eth_string[26:])
    print('Price of Ethereum is')
    print(eth_string)
    print('')
