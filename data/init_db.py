# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 19:48:58 2025

@author: Bart
"""

from connection import get_connection

def init_db():
    conn = get_connection()
    if conn is None:
        print("kan geen verbinding maken")
        return
    
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS categorien (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categorienaam TEXT NOT NULL UNIQUE,
            uitleg TEXT
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS taken (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categorie_id INTEGER,
            titel TEXT NOT NULL,
            status INTEGER NOT NULL,
            FOREIGN KEY (categorie_id) REFERENCES categorien(id)
        )
    """)