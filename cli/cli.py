# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 22:54:41 2025

@author: Bart
"""

from ..data import queries as qry
from ..models.task import Task
from ..models.category import Category

status_tpl = ("to do", "finished", "cancelled") 
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
        print("5. programma sluiten")
        print("6. categorie verwijderen")
        print("7. stop het programma")

        choice = input("\nselecteer optie: ")
        
        if choice =="1":
            categorienaam = input("naam categorie: ")
            uitleg = input("uitleg over categorie: ")
            category = Category(categorienaam = categorienaam, uitleg = uitleg) 
            category.save()
        
        elif choice =="2":
            titel = input("Taak titel:")
            categorie_id = int(input("categorie_id: "))
            task = Task(titel = titel, categorie_id = categorie_id)
            task.save()
            
        elif choice == "7":
            break
    
    
