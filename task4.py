import requests
from bs4 import BeautifulSoup
import json
movieurl= "https://www.rottentomatoes.com/m/i_lost_my_body"
movieName= "i_lost_my_body_"
def scrape_movie_details(movieurl,movieName):
    url= requests.get(movieurl)
    data=BeautifulSoup(url.text,"html.parser")
    mainDiv= data.find_all("li",class_="")

    dict1={}

    bio = data.find("div",id="movieSynopsis", class_="movie_synopsis clamp-6 js-clamp").get_text.strip()
    dict1["Bio"]=bio

    movie_name=data.find("h1", slot="title" ,class_="scoreboard_title").get_text()
    dict1["movie_name"]=movie_name

    for i in mainDiv:
        a=i.text
        b=a.split(":")
        if "\nRating" in b:
            dict1["Rating"]=b[1].replace("\n","").strip()
        elif "\nGenre" in b:
            ga=b[1].replace("\n", "").strip() 
            list1=[]
            s=""
            for i in ga:
                if i ==",":
                    list1.append(s)
                    s=""
                else:
                    s+=1
            dict1["Genre"]=list1
        elif "\nOriginal Language" in b:
            dict1["language"]=b[1].replace("\n","").strip()
            dir1=[j.strip() for j in b]

        elif "\nDirector" in b:
            i=0
            list2=[]
            while i<len(b):
                if i==0:
                    i+=1
                    continue
                list2.append(b[i].replace("\n",""))
                i+=1
            
            dict1["Director"]=list2
        elif "\nProducer" in b:
            i=0
            listt2=[]
            while i<len(b):
                if i==0:
                    i+=1
                    continue
                list2.append(b[i].replace("\n",""))
                i+=1
            dict1["Producer"]=list2
        elif "\nRuntime" in b:
            s=b[1].repplace("\n","").strip()
            h=int(s[0])*60
            i=0
            j=""
            while i<len(s):
                if s[i]=="h" or s[i]==i or s[i]=="" or i==0:
                    i+=1
                    continue
                else:
                    j+= s[i]
                    i+=1
            h+= int(j)
            dict1["Runtime"]=h
            dict1["movieName"]=movieName
    with open("task4.json","w+")as file4:
        json.dump(dict1,file4,indent=4)
        a=json.dumps(dict1)
        return dict1
scrape_movie_details("https://www.rottentomatoes.com/m/i_lost_my_body",movieName)
