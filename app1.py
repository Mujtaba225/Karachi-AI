# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

def main():
    st.title("Hello World1")
    
if __name__=='__main__':
    main()
    
import streamlit as st

def greet_me(name,gender):
    if gender.lower()=='female':
        greeting = "Hello, " + 'Ms.' + name.capitalize()
    else:
        greeting = "Hello, " + 'Ms.' + name.capitalize()
    return greeting

def main():
    st.title("Helllo World")
    name = st.text_input("Name")
    gender = st.selectbox("Gender",["Female","Male"])
    button = st.button("Greet me!")
    if button:
        greeting = greet_me(name,gender)
        st.success(greeting)
        
if __name__=='__main__':
    main()
        
