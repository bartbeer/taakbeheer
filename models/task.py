# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 13:32:00 2025

@author: Bart
"""

import json
import csv

from ..data import queries as qry

class Task:
    
    
    
    def __init__(self, id = None, categorie_id = None, titel=None, status ="todo"):
        self.__id = id
        self.__categorie_id = categorie_id 
        self.__titel = titel
        self.__status = status
        
    def __str__(self):
        return f"[{self.__id}] {self.__titel} | {self.__status} | Category ID: {self.__category_id}"
    
    
    def get_id(self):
        return self.__id
    
    def get_category_id(self):
        return self.__categorie_id
    
    def get_titel(self):
        return self.__titel
    
    def get_status(self):
        return self.__status
    
    def set_category_id(self, categorie_id):
        self.__category_id = categorie_id
        
    def set_titel(self, titel):
        self.__titel = titel
        
    def set_status(self, status):
        self.__status = status
        
    def get_all():
        rows = qry.get_tasks()
        tasks = []
        for row in rows:
            # row = (id, titel, status, categorie_id, categorienaam)
            task_id = row[0]
            titel = row[1]
            status = row[2]
            categorie_id = row[3]
            tasks.append(Task(task_id, categorie_id, titel, status))
        return tasks
    
    def to_dict(self):
        return {
            "id": self.get_id(),
            "titel": self.get_titel(),
            "status": self.get_status(),
            "categorie_id": self.get_category_id(),
            "categorie_naam": qry.get_categorienaam(self.get_category_id()),
        }
    
    @staticmethod
    def get_all_as_dict():
        return [task.to_dict() for task in Task.get_all()]
    
    def export_to_json(pad):
        data = Task.get_all_as_dict()
        if not data:
            print("geen taken aanwezig")
            return
        with open(pad, "w", encoding ="utf-8") as f:
            json.dump(data, f, ensure_ascii = False, indent = 4)
        print(f"json opgeslagen als: {pad}")
    
    def export_to_excel(pad):
        data = Task.get_all_as_dict()
        if not data:
            print("geen taken aanwezig")
            return
        kolommen = data[0].keys()
        
        with open(pad, "w", encoding = "utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=kolommen, delimiter =';')
            writer.writeheader()
            writer.writerows(data)
            
        print(f"excel (CSV) opgeslagen als: {pad}")
    
    def save(self):
            passed = qry.insert_task(self)
            return passed
            
    