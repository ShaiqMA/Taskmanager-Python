# BRONNEN:
# https://www.youtube.com/watch?v=-51jxlQaxyA
# https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
#https://www.geeksforgeeks.org/python/pathlib-module-in-python/
#  https://www.geeksforgeeks.org/python/json-parsing-errors-in-python/

#ik importeer json om json data kan lezen en schrijven
#en ik importeer path uit pathllib module om een path te kunnen maken naar de bestand die ik wil gebruiken
import json
from pathlib import Path

#dit lleidt dus naar me de json bestand waaruit ik data wil ophalen
bestand = Path("data/tasks.json")

#een load tasks functie om de json file te laden
def load_tasks():
    #dit probeert de json map te laden
    try:
        with open(bestand, "r") as f:
            return json.load(f)
    #zo niet krijg je een lege tabel terug
    except FileNotFoundError:
        return []
    #als de bestand een foutje bevat zoals een missende haak krijg je een error terug
    except json.JSONDecodeError:
        print("Fout: bestand is onjuist")
        return []
    
#een save functie om je taken op te slaan in de json file  
def save_tasks(tasks):
    with open(bestand, "w") as f:
        #slaat de taak op met een indenting zodat het beter eruit ziet
        json.dump(tasks, f, indent=4)


