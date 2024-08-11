# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:30:30 2024

@author: jd_se
"""
import streamlit as st
import copy

st.header("2 Player Game")

card_1_1 = "0"
card_1_2 = "0"
card_1_3 = "0"
card_1_4 = "0"
card_2_1 = "0"
card_2_2 = "0"
card_2_3 = "0"
card_2_4 = "0"
card_3_1 = "0"
card_3_2 = "0"
card_3_3 = "0"
card_3_4 = "0"

cards_dict ={"0":"cards/test.jpg",
             "1":"cards/splendor.jpg"}

    
st.write("Please enter cards in colour-cost-points format:\n\n bla/blu/gre/red/whi for colour\n\n a 5 digit number for the cost for the respective colours\n\n a 1 digit number for the points\n\n e.g. blu333001")
    
cols = st.columns(4)
    
with cols[0]:
    initial_card_1_1 = st.text_input("Level 1 Column 1 card")
    initial_card_2_1 = st.text_input("Level 2 Column 1 card")
    initial_card_3_1 = st.text_input("Level 3 Column 1 card")
        
with cols[1]:
    initial_card_1_2 = st.text_input("Level 1 Column 2 card")
    initial_card_2_2 = st.text_input("Level 2 Column 2 card")
    initial_card_3_2 = st.text_input("Level 3 Column 2 card")
        
with cols[2]:
    initial_card_1_3 = st.text_input("Level 1 Column 3 card")
    initial_card_2_3 = st.text_input("Level 2 Column 3 card")
    initial_card_3_3 = st.text_input("Level 3 Column 3 card")
        
with cols[3]:
    initial_card_1_4 = st.text_input("Level 1 Column 4 card")
    initial_card_2_4 = st.text_input("Level 2 Column 4 card")
    initial_card_3_4 = st.text_input("Level 3 Column 4 card")
    
if st.button("Confirm"):
    card_1_1 = copy.deepcopy(initial_card_1_1)
    card_1_2 = copy.deepcopy(initial_card_1_2)
    card_1_3 = copy.deepcopy(initial_card_1_3)
    card_1_4 = copy.deepcopy(initial_card_1_4)
    card_2_1 = copy.deepcopy(initial_card_2_1)
    card_2_2 = copy.deepcopy(initial_card_2_2)
    card_2_3 = copy.deepcopy(initial_card_2_3)
    card_2_4 = copy.deepcopy(initial_card_2_4)
    card_3_1 = copy.deepcopy(initial_card_3_1)
    card_3_2 = copy.deepcopy(initial_card_3_2)
    card_3_3 = copy.deepcopy(initial_card_3_3)
    card_3_4 = copy.deepcopy(initial_card_3_4)

st.subheader("Game Board")
    
level_one = st.columns(4)
level_two= st.columns(4)
level_three = st.columns(4)

with level_one[0]:
    st.image(cards_dict[card_1_1])
    
if st.button("change pic to splendor"):
    with level_one[0]:
        st.image("cards/splendor.jpg")
    
    
    