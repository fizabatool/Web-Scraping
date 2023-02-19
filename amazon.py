import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1",'Accept-Language': 'en-US, en;q=0.5'}
Data = requests.get("https://www.amazon.com/b/ref=s9_acss_bw_cg_SHnav2_2e1_w?node=19185106011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=WXCAV32MVNWHGV5G8G6A&pf_rd_t=101&pf_rd_p=47ed89ed-bbfc-429f-9e64-0c3b9a8ac78e&pf_rd_i=6563140011",headers=headers)
Soup = BeautifulSoup(Products.content,'html.parser')
products = Soup.find_all("div",{'class':"a-section a-spacing-small puis-padding-left-small puis-padding-right-small"})
products


product_links=[]
for product in Allproducts:
        Link = product.find("a",{"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}).get('href')   
        product_links.append(Link)

product_names=[]
for product in Allproducts:
     Name = product.find('span',{'class':'a-size-base-plus a-color-base a-text-normal'})
     product_names.append(Name)

Smart_Devices = {"Name":product_names, 'Link':product_links}

Smart_Devices
df = pd.DataFrame(Smart_Devices)
df
df.to_csv('Devices-Amazon.csv')