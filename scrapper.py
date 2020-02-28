from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://inomics.com/course/business-data-science-summer-school-2020-1430826'
#opening up the connection & grabbing page
myurlvar = uReq(my_url)
page_html = myurlvar.read()
myurlvar.close()
page_soup = soup(page_html, "html.parser")
#grab div class which consist of post summary
#myclass = page_soup.findAll("div",{"class": "post-summary"}
myclass = page_soup.find('div', class_='post-summary').p.text
print(myclass)
sep = page_soup.findAll('time')
print(sep[0])
netherland = page_soup.find('div', class_='location-details').p.text
print(netherland)
taggs = page_soup.find('ul', {'id':'tags'})
print(taggs.text)
summer = page_soup.findAll("div",{"class": "post-details hide-for-small-only"})
print(summer)









