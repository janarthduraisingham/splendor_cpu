# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:30:30 2024

@author: jd_se
"""
import streamlit as st
from PIL import Image, ImageOps

st.header("2 Players Game")

# initialise vars
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
             'turn',
             'obj_1',
             'obj_2',
             'obj_3'
             ]

for var in var_list:
    if var not in st.session_state:
        if var == 'turn':
            st.session_state[var] = 1
        else:
            st.session_state[var] = ''

# List of cards
card_serials = ['bla1002100',
                'blu1300000',
                'gre1010020',
                'whi1112100']

# define card class
class Card:
    
    def __init__(self, serial):
        self.colour = serial[0:3]
        self.level = serial[3]
        self.bla_cost = serial[4]
        self.blu_cost = serial[5]
        self.gre_cost = serial[6]
        self.red_cost = serial[7]
        self.whi_cost = serial[8]
        self.points = serial[9]
        self.image = "cards/" + serial + ".jpg"
    


# create deck of cards (dictionary)
deck = {}

for serial in card_serials:
    
    # instantiate card class
    deck[serial] = Card(serial)
    
    

# confirm button
def confirm_button():
    st.session_state['setup_complete'] = 'complete'

cards_dict ={"":"cards/splendor.jpg",
             "bla1002100":"cards/bla1002100.jpg",
             "blu1300000":"cards/blu1300000.jpg",
             "gre1010020":"cards/gre1010020.jpg",
             "obj300333":"cards/obj300333.jpg",
             "whi1112100":"cards/whi1112100.jpg"}

for key in cards_dict.keys():
    cards_dict[key] = ImageOps.exif_transpose(Image.open(cards_dict[key]))
  

st.write("Open the toggle to set up initial card tableau. Close when done")
if st.toggle("Game setup") and st.session_state['setup_complete']=='': 
    st.write("Please enter cards in colour-cost-points format:\n\n bla/blu/gre/red/whi for colour\n\n a 1 digit number for level\n\n a 5 digit number for the cost for the respective colours\n\n a 1 digit number for the points\n\n e.g. blu1333001")
    
    obj_cols = st.columns(3)
    
    with obj_cols[0]:
        st.session_state['obj_1'] = st.text_input("objective card 1")
        
    with obj_cols[1]:
        st.session_state['obj_2'] = st.text_input("objective card 2")
        
    with obj_cols[2]:
        st.session_state['obj_3'] = st.text_input("objective card 3")
    
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
    
st.subheader("Game Board: Turn " + str(st.session_state['turn']))

obj_tableau = st.columns(3)

with obj_tableau[0]:
    obj_slot_1 = st.empty()
    obj_slot_1.image(cards_dict[st.session_state['obj_1']])
    
with obj_tableau[1]:
    obj_slot_2 = st.empty()
    obj_slot_2.image(cards_dict[st.session_state['obj_2']])
    
with obj_tableau[2]:
    obj_slot_3 = st.empty()
    obj_slot_3.image(cards_dict[st.session_state['obj_3']])
    
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

###############
#def xyz():
#    slot_1_1.empty()
#    st.session_state['card_1_1'] = '1'
#    slot_1_1.image(cards_dict[st.session_state['card_1_1']])
    
#st.button("change 1,1 pic to splendor", on_click=xyz)
###############


st.write("Deck contains: " + str(len(list(deck.keys()))))


    
    