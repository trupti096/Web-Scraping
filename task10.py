from task5 import *

movie_dict={}
movie_list= movie_info

def analyse_director_and_language():
    for name in movie_list:
        count_language=0
        movie_language={}

        for info in movie_list:
            if name["Director"]==info["Director"] and name["language"]==info["Language"]:
                director_name=str(name["Director"])[2:-2]
                language=str(name["Language"])
                count_language+=1
        movie_dict[director_name]=movie_language
    pprint(movie_dict)

    with open("Task10.json","w+") as json_data:
        json.dump(movie_dict,json_data,indent=4)
    return movie_dict
analyse_director_and_language()
