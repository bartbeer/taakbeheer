# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 09:36:04 2025

@author: Bart
"""

from taakbeheer.data.connection import get_connection


class IDNotFoundError(Exception):
    pass

class CategoryNotFoundError(Exception):
    pass

class InvalidCategoryIDError(Exception):
    pass

VALID_STATUSES = ("todo", "done", "cancelled")

def get_categories():
    try:
        with get_connection() as conn:
            mijncursor = conn.cursor()
            read_qry = "SELECT * FROM categorien"    
            rows = mijncursor.execute(read_qry).fetchall()
            return rows
    except Exception as e:
        print(f"Fout bij het ophalen van categorieën: {e}")
        return None
  
def get_tasks():
    try:
        with get_connection() as conn:
            mijncursor = conn.cursor()
            read_qry = "SELECT t.id, t.titel, t.status, c.categorienaam FROM taken t JOIN categorien c ON t.categorie_id = c.id"
            rows = mijncursor.execute(read_qry).fetchall()
            return rows
    except Exception as e:
       print(f"Fout bij het ophalen van taken: {e}") 
       return None

def get_categorienaam(categorie_id):
    try:
        if categorie_id is None:
            raise InvalidCategoryIDError("categorie_id mag niet None zijn.")
        with get_connection() as conn: 
            mijncursor = conn.cursor()
            read_qry = "SELECT categorienaam FROM categorien WHERE id = ?"
            mijncursor.execute(read_qry, (categorie_id,))
            row = mijncursor.fetchone()
            if row is None:
                raise CategoryNotFoundError(f"categorie met id {categorie_id} bestaat niet.")
            
            return row[0]
            
    except CategoryNotFoundError:
        print(f"categorie met id {categorie_id} bestaat niet.")
    except InvalidCategoryIDError as e:
        print(e)
    except Exception as e:
        print(f"Fout bij het ophalen van de categorienaam: {e}")
    
    return None
    
def insert_task(task):
    with get_connection() as conn:
        mijncursor = conn.cursor()
        try:
            # Check if category exists
            mijncursor.execute("SELECT id FROM categorien WHERE id = ?", (task.get_category_id(),))
            if mijncursor.fetchone() is None:
                print(f"Fout: categorie_id {task.get_category_id()} bestaat niet.")
                return False
            
            insert_qry = "INSERT INTO taken (categorie_id, titel, status) VALUES(?,?,?)"
            mijncursor.execute(insert_qry, (task.get_category_id(), task.get_titel(), task.get_status()))
            conn.commit()
            return True
        except Exception as e:
            print(f"fout: {e}")
            return False

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
            return False

    
def delete_task(task_id):
    with get_connection() as conn:
        mijncursor = conn.cursor() 
        try:
            delete_qry = "DELETE FROM taken WHERE id  = ?"
            mijncursor.execute(delete_qry, (task_id,))
            if mijncursor.rowcount == 0:
                raise IDNotFoundError()
            conn.commit()
            return True
        except IDNotFoundError:
            print(f"kan geen taak verwijderen met nummer {task_id}, want deze bestaat niet")
            return False
        except Exception as e:
            print(f"fout: {e}")
            return False
    
def delete_category(cat_id):
    with get_connection() as conn:
        mijncursor = conn.cursor() 
        try:
            delete_qry = "DELETE FROM categorien WHERE id  = ?"
            mijncursor.execute(delete_qry, (cat_id,))
            if mijncursor.rowcount == 0:
                raise IDNotFoundError()
            conn.commit()
            return True
        except IDNotFoundError:
            print(f"kan geen categorie verwijderen met nummer {cat_id}, want deze bestaat niet")
            return False
        except Exception as e:
            print(f"fout: {e}") 
            return False
    
def adjust_task_status(task_id, state):
    with get_connection() as conn:
        mijncursor = conn.cursor()
        try:
            if state not in VALID_STATUSES:
                raise ValueError(f"ongeldige status:'{state}'. " f"Geldige statussen: {', '.join(VALID_STATUSES)}")
                return False
            
            select_qry = "SELECT status from taken WHERE id = ?"
            update_qry = "UPDATE taken SET status = ? WHERE id = ?"
            
            mijncursor.execute(select_qry, (task_id,))
            result = mijncursor.fetchone()
            
            if result is None:
                print(f" de taak met nummer {task_id} bestaat niet.")
                return False
            
            old_result = result[0]
                
            if old_result == state:
                print(f"De taak met nummer {task_id} heeft reeds status '{state}'.")
                return False
            
            mijncursor.execute(update_qry, (state, task_id))
            conn.commit()
            return True
        
        except Exception as e:
            print(f"fout: {e}")
            return False
    








    
    