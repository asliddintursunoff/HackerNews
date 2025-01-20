import pprint
from bs4 import BeautifulSoup
import requests
page_num = input("enter page num: ")
response = requests.get(f"https://news.ycombinator.com/news?p={page_num}")
soup = BeautifulSoup(response.text,'html.parser') 
score1 = soup.select(".subtext")
title = soup.select(".titleline")

def sorted_news_by_votes(lst):
    lst.sort(reverse = True,key = lambda e: e["points"])
    return lst
def hn_app(title,score1):
    lst = []
    
    for idx ,item in enumerate(title):
        h1 = title[idx].getText() 
        link = title[idx].find("a").get('href')
        vote =score1[idx].select(".score")
        
        if len(vote):
           point = vote[0].getText()
           if int(point.replace(" points",""))>100:         
                lst.append({ "title":h1,"link":link,"points" : point})
    return sorted_news_by_votes(lst)
    
pprint.pp(hn_app(title,score1))
  
             
                
                
   
