# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 09:30:47 2025

@author: Bart
"""

import sqlite3
import os

def get_connection():
    """maak een databaseverbinding"""
    
    # absolute pad van de directory waarin dit bestand zich bevindt
    basedir = os.path.dirname(os.path.abspath(__file__))
    
    # het volledige pad naar het databasebestand in dezelfde directory.
    db_path = os.path.join(basedir, 'taken.db')
    
    try:
        conn = sqlite3.connect(db_path)
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