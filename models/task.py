# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 13:32:00 2025

@author: Bart
"""

from ..data import queries as qry

class Task:
    
    VALID_STATUSES = ("todo", "done", "cancelled")
    
    def __init__(self, id = None, categorie_id = None, titel=None, status ="to do"):
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
        return [Task(id, categorie_id, titel, status) for id, categorie_id, titel, status in rows]
    
    def save(self):
            qry.insert_task(self)
    