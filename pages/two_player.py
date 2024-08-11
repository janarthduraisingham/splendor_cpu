# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:30:30 2024

@author: jd_se
"""
import streamlit as st

st.header("2 Player Game")

level_one = st.columns(4)
level_two= st.columns(4)
level_three = st.columns(4)

st.write("Open the toggle below for game setup. Close when done.")
setup_toggle = st.toggle("Game Setup")

initial_level_1_1 = ""
initial_level_1_2 = ""
initial_level_1_3 = ""
initial_level_1_3 = ""

if setup_toggle:
    
    st.write("Please enter cards in colour-cost-points format:\n\n bla/blu/gre/red/whi for colour\n\n a 6 digit number for the cost for the respective colours\n\n a 1 digit number for the points\n\n e.g. blu333001")
    
    cols = st.columns(4)
    
    with cols[0]:
        initial_level_1_1 = st.text_input("Level 1 Column 1 card")
        initial_level_2_1 = st.text_input("Level 2 Column 1 card")
        
    with cols[1]:
        initial_level_1_2 = st.text_input("Level 1 Column 2 card")
        
    with cols[2]:
        initial_level_1_3 = st.text_input("Level 1 Column 3 card")
        
    with cols[3]:
        initial_level_1_4 = st.text_input("Level 1 Column 4 card")
    
    
    
st.write("value of row 1: " + initial_level_1_1 + initial_level_1_2 + initial_level_1_3 + initial_level_1_4)
    

    
    