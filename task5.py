from task2 import group_by_year
from task4 import*
from task1 import movie_data
from pprint import pprint

movie=movie_data
user=int(input("enter how many you eant"))
def get_movie_list_details():
    movie_url=[]
    movie_list=[]
    i=0
    while i<len(movie[:user]):
        movie_list.append(scrape_movie_details(movie_data[i]["url"],movie_data[i]["Movie_Name"]))
    with open("task5.json","w+") as movie_details:
        json.dump(movie_list,movie_details,indent=4)

    return movie_list
movie_info=get_movie_list_details()

#task5
