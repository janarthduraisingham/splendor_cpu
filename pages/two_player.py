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

setup_toggle = st.toggle("Setup Complete!")

test = "unedited"

if setup_toggle:
    
    st.write("setup not complete")
    
    test = st.text_input("edit test variable")
    
st.write("value of test variable is " + test)
    

    
    