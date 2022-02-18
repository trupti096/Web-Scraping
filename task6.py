from task5 import *

file=open("task5.json")
data=json.load(file)

def analyse_movie_language(data):
    language_dict={}

    i=0
    while i<len(data):
        index=0
        count=1
        while index<len(data):
            if data[i]["language"]==data[index]["language"]:
                count+=1
                language=str(data[i]["language"])[0:]
                language_dict[language]=count
            index+=1
        i+=1
    with open("task6.json","w+") as language_data:
        json.dump(language_dict,language_data,indent=4)

    return language_dict
analyse_movie_language(data)

#task6
