import requests 
from bs4 import BeautifulSoup 
import re
from pandas import DataFrame
URL = "http://www.virusign.com/home.php?d=0&r=100&c=hashes&o=date&s=DESC&n=EXACT&p=1"
r = requests.get(URL) 
#print(r.headers['Set-Cookie'])
src = r.content
soup = BeautifulSoup(src,'html5lib')



#table = soup.find('tr',{'data-index':'0'})
#print(table.find('td').text)

table = soup.find('tbody')
#ßprint(table)
a_tag = []
children = table.findChildren('tr',recursive=False)
#print(children)

for child in children:
    data = child.find_all("td")
    #print(data)
    #if data.findChild("a",recursive=False) != None:
    for item in data:
        if item:
            a = item.findChild("a")
            if a:
                h_ref = a.get('href')
                if h_ref.startswith("details"):
                    a_tag.append(h_ref)


#print(a_tag)
#print(len(a_tag))
res = []
for link in a_tag:
    url = "https://virusign.com/"+link
    print(url)
    r = requests.get(url) 
    #print(r.headers['Set-Cookie'])
    src = r.content
    soup = BeautifulSoup(src,'html5lib')
    table = soup.find('tbody')
    children = table.findChildren("tr",recursive=False)
    a = []
    for child in children:
        th = child.findChild("th")
        data = child.findChild("td")
        if th.text == "Name":
            a.append((data.text))
        elif th.text.find("Date") != -1:
            a.append((data.text))
        elif th.text.find("Size") != -1:
            a.append((data.text))
        elif data:
            text = data.text
            x = re.search("^[A-Fa-f0-9]{32}$",text)
            y = re.search("^[A-Fa-f0-9]{64}$",text)
            u = re.search("^[A-Fa-f0-9]{40}$",text)
            z = re.search("[0]{32}",text)
            if x and z == None:
                a.append((text))
            elif y and x == None and z == None:
                a.append((text))
            elif x == None and y == None and z == None and u:
                a.append((text))
    if len(a)!=0:
        res.append(list(a))
print(res)
df = DataFrame.from_records(res)
df.to_csv("/Users/gokulakrishnan.parir/Desktop/Scrap_virus_sign.csv") 





