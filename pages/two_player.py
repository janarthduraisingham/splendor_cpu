# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:30:30 2024

@author: jd_se
"""
import streamlit as st
#import copy

st.header("2 Player Game")

# initialise 3x4 card tableau
var_list = ['card_1_1',
             'card_1_2',
             'card_1_3',
             'card_1_4',
             'card_2_1',
             'card_2_2',
             'card_2_3',
             'card_2_4',
             'card_3_1',
             'card_3_2',
             'card_3_3',
             'card_3_4',
             'setup_complete',
             'turn'
             ]

for var in var_list:
    if var not in st.session_state:
        if var == 'turn':
            st.session_state[var] = 1
        else:
            st.session_state[var] = ''
            
# confirm button
def confirm_button():
    st.session_state['setup_complete'] = 'complete'

cards_dict ={"":"cards/splendor.jpg",
             "bla002100":"cards/bla002100.jpg",
             "blu300000":"cards/blu300000.jpg",
             "gre010020":"cards/gre010020.jpg",
             "obj300333":"cards/obj300333.jpg",
             "whi112100":"cards/whi112100.jpg"}


st.write("Open the toggle to set up initial card tableau. Close when done")
if st.toggle("Game setup") and st.session_state['setup_complete']=='': 
    st.write("Please enter cards in colour-cost-points format:\n\n bla/blu/gre/red/whi for colour\n\n a 5 digit number for the cost for the respective colours\n\n a 1 digit number for the points\n\n e.g. blu333001")
    
    cols = st.columns(4)
        
    with cols[0]:
        st.session_state['card_1_1'] = st.text_input("Level 1 Column 1 card")
        st.session_state['card_2_1'] = st.text_input("Level 2 Column 1 card")
        st.session_state['card_3_1'] = st.text_input("Level 3 Column 1 card")
        
    with cols[1]:
        st.session_state['card_1_2'] = st.text_input("Level 1 Column 2 card")
        st.session_state['card_2_2'] = st.text_input("Level 2 Column 2 card")
        st.session_state['card_3_2'] = st.text_input("Level 3 Column 2 card")
        
    with cols[2]:
        st.session_state['card_1_3'] = st.text_input("Level 1 Column 3 card")
        st.session_state['card_2_3'] = st.text_input("Level 2 Column 3 card")
        st.session_state['card_3_3'] = st.text_input("Level 3 Column 3 card")
            
    with cols[3]:
        st.session_state['card_1_4'] = st.text_input("Level 1 Column 4 card")
        st.session_state['card_2_4'] = st.text_input("Level 2 Column 4 card")
        st.session_state['card_3_4'] = st.text_input("Level 3 Column 4 card")
        
    st.button("Confirm setup", on_click=confirm_button)
    
#if st.button("Confirm"):
#    card_1_1 = copy.deepcopy(initial_card_1_1)
#    card_1_2 = copy.deepcopy(initial_card_1_2)
#    card_1_3 = copy.deepcopy(initial_card_1_3)
#    card_1_4 = copy.deepcopy(initial_card_1_4)
#    card_2_1 = copy.deepcopy(initial_card_2_1)
#    card_2_2 = copy.deepcopy(initial_card_2_2)
#    card_2_3 = copy.deepcopy(initial_card_2_3)
#    card_2_4 = copy.deepcopy(initial_card_2_4)
#    card_3_1 = copy.deepcopy(initial_card_3_1)
#    card_3_2 = copy.deepcopy(initial_card_3_2)
#    card_3_3 = copy.deepcopy(initial_card_3_3)
#   card_3_4 = copy.deepcopy(initial_card_3_4)

st.subheader("Game Board: Turn " + str(st.session_state['turn']))
    
tableau = st.columns(4)

with tableau[0]:
    slot_1_1 = st.empty()
    slot_1_1.image(cards_dict[st.session_state['card_1_1']])
    
    slot_2_1 = st.empty()
    slot_2_1.image(cards_dict[st.session_state['card_2_1']])
    
    slot_3_1 = st.empty()
    slot_3_1.image(cards_dict[st.session_state['card_3_1']])
    
with tableau[1]:
    slot_1_2 = st.empty()
    slot_1_2.image(cards_dict[st.session_state['card_1_2']])
    
    slot_2_2 = st.empty()
    slot_2_2.image(cards_dict[st.session_state['card_2_2']])
    
    slot_3_2 = st.empty()
    slot_3_2.image(cards_dict[st.session_state['card_3_2']])
    
with tableau[2]:
    slot_1_3 = st.empty()
    slot_1_3.image(cards_dict[st.session_state['card_1_3']])
    
    slot_2_3 = st.empty()
    slot_2_3.image(cards_dict[st.session_state['card_2_3']])
    
    slot_3_3 = st.empty()
    slot_3_3.image(cards_dict[st.session_state['card_3_3']])
    
with tableau[3]:
    slot_1_4 = st.empty()
    slot_1_4.image(cards_dict[st.session_state['card_1_4']])
    
    slot_2_4 = st.empty()
    slot_2_4.image(cards_dict[st.session_state['card_2_4']])
    
    slot_3_4 = st.empty()
    slot_3_4.image(cards_dict[st.session_state['card_3_4']])

def xyz():
    slot_1_1.empty()
    st.session_state['card_1_1'] = '1'
    slot_1_1.image(cards_dict[st.session_state['card_1_1']])
    
st.button("change 1,1 pic to splendor", on_click=xyz)

st.write("session state:")    
st.write(st.session_state)
    
    