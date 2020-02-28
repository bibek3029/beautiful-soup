from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://inomics.com/course/business-data-science-summer-school-2020-1430826'
#opening up the connection & grabbing page
myurlvar = uReq(my_url)
page_html = myurlvar.read()
myurlvar.close()
page_soup = soup(page_html, "html.parser")
#this takes you to to get title of the page
a = page_soup.title.text
print(a)
#grab div class which consist of post summary
#myclass = page_soup.findAll("div",{"class": "post-summary"}
#here we get the first paragram text
myclass = page_soup.find('div', class_='post-summary').p.text
print(myclass)
#sep variable gives you the time 8th june 2020
sep = page_soup.findAll('time')
print(sep[0])
#now scrapping netherland from the website
netherland = page_soup.find('div', class_='location-details').p.text
print(netherland)
#for getting political science, deeplearning all five from below
taggs = page_soup.find('ul', {'id':'tags'})
print(taggs.text)
#now to get summer school we go through below process
myhead = page_soup.find('div', {'class':'post-details hide-for-small-only'}, 'div')
a= myhead.findAll('h4')
print(a[4])
#now for getting website link we go through following process
wwebsite = page_soup.find('div', class_='small-16 apply')
print(wwebsite.p.a)









