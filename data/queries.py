# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 09:36:04 2025

@author: Bart
"""

from taakbeheer.data.connection import get_connection


class IDNotFoundError(Exception):
    pass

class TaskStatusUnchanged(Exception):
    pass

VALID_STATUSES = ("todo", "done", "cancelled")

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

def get_categorienaam(categorie_id):
    with get_connection() as conn: 
        mijncursor = conn.cursor()
        read_qry = "SELECT categorienaam FROM categorien WHERE id = ?"
        mijncursor.execute(read_qry, (categorie_id,))
        row = mijncursor.fetchone()
        return row[0] if row else None

def insert_task(task):
    with get_connection() as conn:
        mijncursor = conn.cursor()
        try:
            insert_qry = "INSERT INTO taken (categorie_id, titel, status) VALUES(?,?,?)"
            mijncursor.execute(insert_qry, (task.get_category_id(), task.get_titel(), task.get_status()))
            conn.commit()
            return True
        except Exception as e:
            print(f"fout: {e}")

def insert_category(category):
    with get_connection() as conn:
        mijncursor = conn.cursor()
        try:
            insert_qry = "INSERT INTO categorien (categorienaam, uitleg) VALUES (?,?)"
            mijncursor.execute(insert_qry, (category.get_categorienaam(), category.get_uitleg()))
            conn.commit()
            return True
        except Exception as e:
            print(f"fout: {e}")

  
def insert_new_category():
    print('nieuwe categorie toevoegen')
    
def delete_task(task_id):
    with get_connection() as conn:
        mijncursor = conn.cursor() 
        try:
            delete_qry = "DELETE FROM taken WHERE id  = ?"
            mijncursor.execute(delete_qry, (task_id,))
            if mijncursor.rowcount == 0:
                raise IDNotFoundError()
            conn.commit()
        except IDNotFoundError:
            print(f"kan geen taak verwijderen met nummer {task_id}, want deze bestaat niet")
        except Exception as e:
            print(f"fout: {e}")
    
def delete_category(cat_id):
    with get_connection() as conn:
        mijncursor = conn.cursor() 
        try:
            delete_qry = "DELETE FROM categorien WHERE id  = ?"
            mijncursor.execute(delete_qry, (cat_id,))
            if mijncursor.rowcount == 0:
                raise IDNotFoundError()
            conn.commit()
        except IDNotFoundError:
            print(f"kan geen categorie verwijderen met nummer {cat_id}, want deze bestaat niet")
        except Exception as e:
            print(f"fout: {e}") 
    
def adjust_task_status(task_id, state):
    with get_connection() as conn:
        mijncursor = conn.cursor()
        try:
            select_qry = "SELECT status from taken WHERE id = ?"
            update_qry = "UPDATE taken SET status = ? WHERE id = ?"
            mijncursor.execute(select_qry, (task_id,))
            result = mijncursor.fetchone()
            if result is None:
                raise IDNotFoundError()
                
            if result[0] == state:
                raise TaskStatusUnchanged()
            
            mijncursor.execute(update_qry, (state, task_id))
            if mijncursor.rowcount == 0:
                raise IDNotFoundError()

            conn.commit()
            return True
        except IDNotFoundError:
            print(f"de taak met nummer {task_id} bestaat niet")
        except TaskStatusUnchanged:
            print(f"de taak met nummer {task_id} heft reeds de status: {state}")
        except Exception as e:
            print(f"fout: {e}")
    
def adjust_category_name_and_expanation():
    print('categorienaam en/of uitleg aanpassen')







    
    