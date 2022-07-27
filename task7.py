from task5 import *

file= open("task5.json")
data=json.load(file)

def analyse_movies_directors():
    director_dic={}

    i=0
    while i<len(data):
        count=1
        index=0
        while index<len(data):
            if data[i]["director"]==data[index]["director"]:
                count+=1
                director=str(data[i]["director"])[2:-2]
                director_dic[director]=count
            index+=1
        i+=1
    with open("Task7.json","w+") as Director_info:
        json.dump(director_dic.director_info,indent=4)
        return director_dic

analyse_movies_directors()
