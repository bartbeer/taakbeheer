# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 19:48:58 2025

@author: Bart
"""

from .connection import get_connection

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
            status TEXT NOT NULL,
            FOREIGN KEY (categorie_id) REFERENCES categorien(id)
        )
    """)

    cur.execute("SELECT COUNT(*) FROM categorien")
    if cur.fetchone()[0] == 0:
        cur.execute(
            "INSERT INTO categorien (categorienaam, uitleg) VALUES (?, ?)",
            ("Algemeen", "Standaard categorie voor nieuwe taken")
        )
        
    cur.execute("SELECT COUNT(*) FROM taken")
    if cur.fetchone()[0] == 0:
        # Haal ID van de standaardcategorie
        cur.execute("SELECT id FROM categorien WHERE categorienaam = ?", ("Algemeen",))
        categorie_id = cur.fetchone()[0]
        cur.execute(
            "INSERT INTO taken (categorie_id, titel, status) VALUES (?, ?, ?)",
            (categorie_id, "Welkomstaak", "todo")
        )    
    
    conn.commit()
    conn.close()
    print("Database succesvol geïnitialiseerd met standaarddata.")