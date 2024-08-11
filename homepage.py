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

cols = st.columns(3)

with cols[0]:
    if st.button("New 2 player game"):   
        st.navigation("pages/two_player.py")
    
with cols[1]:
    if st.button("New 3 player game"):
        st.navigation("pages/three_player.py")
    
with cols[2]:
    if st.button("New 4 player game"):
        st.navigation("pages/four_player.py")

homepage = st.Page("homepage.py", title="Splendor CPU", icon=":material/diamond:")
two_player = st.Page("pages/two_player.py", title="2 Player Game", icon=":material/diamond:")
three_player = st.Page("pages/three_player.py", title="3 Player Game", icon=":material/diamond:")
four_player = st.Page("pages/four_player.py", title="4 Player Game", icon=":material/diamond:")


pg = st.navigation([
                    homepage,
                    two_player,
                    three_player,
                    four_player
                    ])
                   
pg.run()