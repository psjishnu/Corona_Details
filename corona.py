import sys 
import requests 
from bs4 import BeautifulSoup 
import json

x=(sys.argv[1])
y=(sys.argv[2])

country=x
URL = "https://coronavirus-tracker-api.herokuapp.com/a1"
URL = URL.replace("a1",y)
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') 

p=soup.prettify()
p=p.replace("<body>",'')
p=p.replace("</body>",'')
p=p.replace("<head>",'')
p=p.replace("</head>",'')
p=p.replace("<html>",'')
p=p.replace("</html>",'')

y = json.loads(p)
y = json.dumps(y)
y= json.loads(y)
y=str(y["locations"])
y=json.dumps(y)

x=0
length=len(country)
x=len(y)
i=0
i1=0
j=0
j1=0
sum=0
for i in range (0,x) :
    if(y[i]==country[0]):
        j=i
        if(y[j:j+length:1]==country and y[j+length]=='\'' and y[j-1]=='\''):
            for i1 in range(i,x):
                if(y[i1]=='l'):
                    j1=i1
                    if(y[j1:j1+6:1]=="latest"):
                        l1=j1+9
                        while(y[l1]!=' '):
                            l1=l1+1
                        sum=sum+int(y[j1+9:l1-1])
                        break

print(sum)
