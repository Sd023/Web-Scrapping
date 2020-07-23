from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

laptopName=[] 
prices=[] 

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
driver.get("https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&sort=popularity&p%5B%5D=facets.offer_type%255B%255D%3DExchange%2BOffer&p%5B%5D=facets.brand%255B%255D%3DSony&otracker=hp_banner_1_12.bannerX3.BANNER_Y4C1R8EXMU54&fm=neo%2Fmerchandising&iid=M_672709c9-d00a-44f6-9728-f84743ca2e6a_12.Y4C1R8EXMU54&ppt=hp&ppn=homepage&ssid=iizwtiqvxc0000001595486300377")
content = driver.page_source

soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_31qSD5'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    
    laptopName.append(name.text)
    prices.append(price.text)
  
df = pd.DataFrame({'Product Name':laptopName,'Price':prices}) 
df.to_csv('Products.csv', index=False, encoding='utf-8')
