# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:36:28 2024

@author: tkannand
"""

import streamlit as st
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('names.db')
c = conn.cursor()

# Create a table to store names if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS names (name TEXT)''')
conn.commit()

def insert_name(name):
    """Insert a name into the database."""
    c.execute('INSERT INTO names (name) VALUES (?)', (name,))
    conn.commit()

def get_names():
    """Retrieve all names from the database."""
    c.execute('SELECT name FROM names')
    return c.fetchall()

# Streamlit app interface
st.title('Name Storage App')

# User input
user_name = st.text_input('Enter your name')

# Button to insert name into the database
if st.button('Submit'):
    insert_name(user_name)
    st.success(f'Name {user_name} added to the database!')

# Displaying names stored in the database
st.write('Names in database:')
names = get_names()
for name in names:
    st.write(name[0])

# It's important to close the connection to the database when you're done
def close_connection():
    c.close()
    conn.close()

st.sidebar.button('Close database connection', on_click=close_connection)
