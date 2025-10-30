# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 09:30:47 2025

@author: Bart
"""

import sqlite3

DATABASE_FILE = "taken.db"

def get_connection():
    """maak een databaseverbinding"""
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        return conn
    except sqlite3.Error as e:
        print(f"fout bij connecteren met database: {e}")
        return None
    
def test_connection():
    conn = get_connection()
    if conn:
        print("gelukt")
        conn.close()
        return True
    else:
        print("helaas niet gelukt")
        return False