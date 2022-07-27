from task1 import movie_data
import json
# import pprint
file1=open("task1.json")
movies=json.load(file1)
def group_by_year(movies):
    empty_dic={}
    for index in movies:
        movie_list=[]
        year=index["Year"]
        if year not in empty_dic:
            for k in movies:
                if year==k["Year"]:
                    movie_list.append(k)
            empty_dic[year]=movie_list
    with open("task2.json","w+") as file:
        json.dump(empty_dic,file,indent=4)
        a=json.dumps(empty_dic)
year_=group_by_year(movie_data)
