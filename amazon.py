from bs4 import BeautifulSoup
import requests
from requests_html import HTML, HTMLSession


with open('amazon.html','r')as html_file:
    content = html_file.read()

soup = BeautifulSoup(content,'html.parser')

bookname = soup.find_all('span',class_='a-size-medium a-color-base a-text-normal')
for name in bookname:
    print('bookname:' ,name.text+'\n')

authors = soup.find_all('a',class_='a-size-base a-link-normal')
for author in authors:
    print('author:' ,author.attrs['href']+'\n')


productlink = soup.find_all('a',class_='a-link-normal s-no-outline')
for product in productlink:
    print('productlink:' ,product.attrs['href']+'\n')


images = soup.find_all('img')
for image in images: 
    print('imagelink:',image.attrs['src']+'\n')
    

prices = soup.find_all('span',class_='a-price-whole')
for price in prices:
    print('price:' ,price.text+'\n')


