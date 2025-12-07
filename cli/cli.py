# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 22:54:41 2025

@author: Bart
"""
import os
from taakbeheer.data.connection import get_connection

from ..data import queries as qry
from ..models.task import Task
from ..models.category import Category
from ..data.init_db import init_db


status_tpl = ("todo", "done", "cancelled") 


def main():
    
    init_db()
    
    while True:
        print("\nwelkom in taakbeheer".upper())
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
            if not categorienaam:
                print("categorienaam mag niet leeg zijn")
                input("\n✅ Druk op Enter om verder te gaan")
                continue
            
            uitleg = input("uitleg over categorie: ")
            if not uitleg:
                print("uitleg mag niet leeg zijn")
                input("\n✅ Druk op Enter om verder te gaan")
                continue
            
            category = Category(categorienaam = categorienaam, uitleg = uitleg) 
            if category.save():
                input("\n✅ Categorie toegevoegd. Druk op Enter om te verversen...")
            continue
        
        elif choice =="2":
            titel = input("Taak titel:")
            if not titel:
                print("titel mag niet leeg zijn")
                input("\n✅ Druk op Enter om verder te gaan")
                continue
            categorie_id = int(input("categorie_id: "))
            task = Task(titel = titel, categorie_id = categorie_id)
            if task.save():
                input("\n✅ Taak toegevoegd. Druk op Enter om te verversen...")
            continue
         
        elif choice == "3":
            print("mogelijke status:\n")
            for i, status in enumerate(status_tpl):
                print(f"{i} - {status}")        
            try:
                taak = input("taaknummer: ")
                if not taak.isdigit():
                    print("Ongeldige invoer: taaknummer moet een getal zijn.")
                    continue
                
                taaknummer = int(taak)
                
                status = input("nummer status: ")
                if not status.isdigit():
                    print("Ongeldige invoer: status moet een getal zijn.")
                    continue                   
                
                status_index = int(status)
                if not (0 <= status_index < len(status_tpl)):
                    print(f"Ongeldige keuze, kies een getal tussen 0 en {len(status_tpl)-1}")
                    continue
                 
                nieuwe_status = status_tpl[status_index]
                succes = qry.adjust_task_status(taaknummer, nieuwe_status)
                    
                if succes:
                    input("\n✅ Status aangepast. Druk op Enter om te verversen...")
                else:
                    print("Kon status niet aanpassen. Zie melding hierboven.")
            except ValueError:
                print("ongeldige invoer")
            continue
        
        elif choice == "4":         
            try:
                id_str = input("geef het nummer van de taak die je wil verwijderen: ")
                if not id_str.isdigit():
                    print("Ongeldige invoer: taaknummer moet een getal zijn.")
                    continue
                taak_id = int(id_str)
        
                confirm = input(f"Weet je zeker dat je taak {taak_id} wilt verwijderen? (ja/nee): ").strip().lower()
                if confirm != "ja":
                    print("Verwijderen geannuleerd.")
                    continue
                succes = qry.delete_task(taak_id)
                
                if succes:
                    input("\n✅ taak verwijderd. Druk op Enter om te verversen...")
            
            except ValueError:
                print("ongeldige invoer")
            continue
        
        elif choice == "5":
            try:
                id = input("geef het nummer van de categorie die je wil verwijderen: ")
                if not id.isdigit():
                    print("Ongeldige invoer: categorienummer moet een getal zijn.")
                cat_id = int(id)
                
                confirm = input(f"Weet je zeker dat je de categorie {cat_id} wilt verwijderen? (ja/nee): ").strip().lower()
                if confirm != "ja":
                    print("Verwijderen geannuleerd.")
                    continue
                succes = qry.delete_category(cat_id)
                
                if succes:
                    input("\n✅ categorie verwijderd. Druk op Enter om te verversen...")
            
            except ValueError:
                print("ongeldige invoer")
            continue 
        elif choice == "6":
            Task.export_to_json("taken.json")
            continue
       
        elif choice == "7":
            Task.export_to_excel("taken.csv")        
            continue
        
        elif choice == "8":
            break
    
    
