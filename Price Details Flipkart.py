import requests
from bs4 import BeautifulSoup
import csv

search = input("What you want to search?")
i = 1
abc = [1,2,3,4,5]
z = 1
dict = []
url2 = "https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page=" + str(i) + "&q=" + str(search)  + "&viewType=list"
k = requests.get(url2)
for i in abc:
	url2 = "https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page=" + str(i) + "&q=" + str(search)  + "&viewType=list"
	k = requests.get(url2)
	soup = BeautifulSoup(k.content, "html5lib")
	data2 = soup.find_all("div", {"class": "col _2-gKeQ"})
	for item2 in data2:
		for z in range(1):
			dic = {}
			dic['Name'] = str(item2.contents[0].find_all("div", {"class": "_3wU53n"})[0].text) 
			dic['Price'] = str(item2.contents[0].find_all("div", {"class": "_1vC4OE _2rQ-NK"})[0].text)
			dict.append(dic)




 




fields = ['Name', 'Price']

with open("Prics.csv", "w") as f:
	writer = csv.DictWriter(f, fieldnames = fields)
	writer.writeheader()
	writer.writerows(dict)






