# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 14:00:27 2025

@author: Bart
"""

from ..data import queries as qry

class Category:
    def __init__(self, id=None, categorienaam="", uitleg =""):
        self.__id = id
        self.__categorienaam = categorienaam
        self.__uitleg = uitleg
        
    def get_id(self):
        return self.__id
    
    def get_categorienaam(self):
        return self.__categorienaam
    
    def get_uitleg(self):
        return self.__uitleg
    
    def set_categorienaam(self, categorienaam):
        self.__categorienaam = categorienaam
        
    def set_uitleg(self, uitleg):
        self.__uitleg = uitleg
        
    def save(self):
        qry.insert_category(self)
        
        