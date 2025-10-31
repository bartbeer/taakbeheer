# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 09:36:04 2025

@author: Bart
"""

from taakbeheer.data.connection import get_connection



def get_categories():
    with get_connection() as conn:
        mijncursor = conn.cursor()
        read_qry = "SELECT * FROM categorien"    
        rows = mijncursor.execute(read_qry).fetchall()
        return rows
    
def get_tasks():
    with get_connection() as conn:
        mijncursor = conn.cursor()
        read_qry = "SELECT t.id, t.titel, t.status, c.categorienaam FROM taken t JOIN categorien c ON t.categorie_id = c.id"
        rows = mijncursor.execute(read_qry).fetchall()
        return rows
    
def insert_task(task):
    with get_connection() as conn:
        mijncursor = conn.cursor()
        insert_qry = "INSERT INTO taken (categorie_id, titel, status) VALUES(?,?,?)"
        try:
            mijncursor.execute(insert_qry, (task.get_category_id(), task.get_titel(), task.get_status()))
            conn.commit()
            return True
        except Exception as e:
            print(f"error: {e}")

def insert_category(category):
    with get_connection() as conn:
        mijncursor = conn.cursor()
        insert_qry = "INSERT INTO categorien (categorienaam, uitleg) VALUES (?,?)"
        try:
            mijncursor.execute(insert_qry, (category.get_categorienaam(), category.get_uitleg()))
            conn.commit()
            return True
        except Exception as e:
            print(f"erroro: {e}")

  
def insert_new_category():
    print('nieuwe categorie toevoegen')
    
def delete_task():
    print('taak verwijderen')
    
def delete_category():
    print('verwijder categorie')
    
def adjust_task_status():
    print('taak status en/of titel aanpassen')
    
def adjust_category_name_and_expanation():
    print('categorienaam en/of uitleg aanpassen')







    
    