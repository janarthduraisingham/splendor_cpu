# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:51:36 2024

@author: jd_se
"""
import streamlit as st


st.set_page_config(page_title="Splendor CPU", page_icon=":gem:",
                   initial_sidebar_state='collapsed')

st.title("Splendor: CPU system")

st.write ("M. Andre (2014). Splendor [Board Game]. Space Cowboys")

st.write("Choose game:")

if st.button("New 2 player game"):
    
    st.navigate("pages/two_player")


