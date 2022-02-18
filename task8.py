import requests
from bs4 import BeautifulSoup
import json
import os
from task1 import  movie_data, scrape_top_list 
from task4 import scrape_movie_details

movie = scrape_top_list()

def get_movie_list_details():
    movie_list=[]
    for i in movie:
        path="/home/dell27/WEPSCRAPPING/allmovie.text"+i["Movie_Name"]+".text"
        if os.path.exists("file.json"):
            pass
        else:
            create= open("/home/dell27/WEPSCRAPPING/allmovie.text"+i["Movie_Name"]+".text","w")
            url=requests.get(i["Url"])
            print(i["Url"])
            create1=create.write(url.text)
            create.close()
            a= scrape_movie_details(i["Movie_Name"],i["Url"])
            movie_list.append(a)
        with open("task","w+") as file5:
            json.dump(movie_list,file5,indent=4)
            print(movie_list)
get_movie_list_details()

#task8
