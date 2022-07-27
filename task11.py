from task5 import *

genre_info= movie_info

def analyse_movie_genre():
    genre_dict={}
    for data in genre_info:

        count=0
        for genre in data["Genre"]:
            for check_genre in data["Genre"]:
                if genre==check_genre:
                    count+=1
            genre_dict[genre]=count
    
    with open("task11.json","w+") as genre_data:
        json.dump(genre_dict,genre_data,indent=4)
    pprint(genre_dict)
    return genre_dict

analyse_movie_genre()
