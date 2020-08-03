##Importing Libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

##Creating a Empty Array
productName=[] 
productPrice=[] 

##Starting the Crhome driver
driver = webdriver.Chrome('Path of the chrome driver')##Give the Path where the chrome driver is installed
driver.get("https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&sort=popularity&p%5B%5D=facets.offer_type%255B%255D%3DExchange%2BOffer&p%5B%5D=facets.brand%255B%255D%3DSony&otracker=hp_banner_1_12.bannerX3.BANNER_Y4C1R8EXMU54&fm=neo%2Fmerchandising&iid=M_672709c9-d00a-44f6-9728-f84743ca2e6a_12.Y4C1R8EXMU54&ppt=hp&ppn=homepage&ssid=iizwtiqvxc0000001595486300377")
content = driver.page_source

soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}): ##finding all the data under tag <a> and Class
    
    name=a.find('div', attrs={'class':'_31qSD5'}) ##Creating a variable and storing the elements under <div> tag and class
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'}) ##Creating the variable and storing the elements under <div> tag and class
    
    productName.append(name.text) ##Appending the data to the Empty Array
    productPrice.append(price.text)
  
df = pd.DataFrame({'Product Name':productName,'Price':productPrice}) ##creating a DataFrame to store the data 
df.to_csv('Products.csv', index=False, encoding='utf-8')##Storing the data in CSV format
