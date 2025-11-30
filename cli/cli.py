# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 22:54:41 2025

@author: Bart
"""

from ..data import queries as qry
from ..models.task import Task
from ..models.category import Category


status_tpl = ("todo", "finished", "cancelled") 
opdrachten_tpl = ("1 - taak toevoegen", "2 - taak wijzigen" , "3 - taak verwijeren" , "4 - ")

def main():
    
    while True:
        print("welkom in taakbeheer".upper())
        print('hieronder de verschillende categorien:\n')
    
        cat = qry.get_categories()
        tasks = qry.get_tasks()
    
        if not cat:
            print('er zijn geen categorien')
    
        if cat: 
            print("id "+"-"+" categorie "+"-"+" uitleg")
            for e in cat:
                print(e[0] ,"-", e[1] ,"-", e[2])
        
        print('\nhieronder alle taken die je al hebt:\n')
    
        if not tasks:
            print('er zijn geen taken')
        if tasks:
            print("id "+"-"+" titel "+"-"+" status "+"-"+" categorienaam")
            for e in tasks:
                print(e[0] ,"-", e[1] ,"-", e[2] ,"-", e[3])
    
        print('\nwat wil je doen?\n')
        print("1. categorie toevoegen")
        print("2. taak toevoegen")
        print("3. taak status veranderen")
        print("4. taak verwijderen")
        print("5. categorie verwijderen")
        print("6. export tasks to json file")
        print("7. export tasks to excel")
        print("8. stop het programma")

        choice = input("\nselecteer optie: ")
        
        if choice =="1":
            categorienaam = input("naam categorie: ")
            uitleg = input("uitleg over categorie: ")
            category = Category(categorienaam = categorienaam, uitleg = uitleg) 
            category.save()
            input("\n✅ Categorie toegevoegd. Druk op Enter om te verversen...")
            continue
        
        elif choice =="2":
            titel = input("Taak titel:")
            categorie_id = int(input("categorie_id: "))
            task = Task(titel = titel, categorie_id = categorie_id)
            task.save()
            input("\n✅ Taak toegevoegd. Druk op Enter om te verversen...")
            continue
         
        elif choice == "3":
            print("mogelijke status:\n")
            for e in status_tpl:
                print(e)
            id = int(input("taaknummer: "))
            status = input("naam status: ")
            qry.adjust_task_status(id, status)
            input("\n✅ Status aangepast. Druk op Enter om te verversen...")
            continue
        
        elif choice == "4":
            id = int(input("geef het nummer van de taak die je wil verwijderen: "))
            qry.delete_task(id)
            input("\n✅ taak verwijderd. Druk op Enter om te verversen...")
            continue
        
        elif choice == "5":
            id = int(input("geef het nummer van de categorie die je wil verwijderen: "))
            qry.delete_category(id)
            input("\n✅ categorie verwijderd. Druk op Enter om te verversen...")
            continue
 
        elif choice == "6":
            Task.export_to_json("taken.json")
            continue
       
        elif choice == "7":
            Task.export_to_excel("taken.csv")        
            continue
        
        elif choice == "8":
            break
    
    
