# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:30:30 2024

@author: jd_se
"""
import streamlit as st
from PIL import Image, ImageOps

st.header("2 Player Game")

# initialise blank string vars
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
            'obj_3',
            'p1_deck',
            'p1_reserve_deck',
            'cpu_deck',
            'cpu_reserve_deck',
            'initialise',
            'cpu_black',
            'cpu_blue',
            'cpu_green',
            'cpu_red',
            'cpu_white',
            'cpu_gold',
            'p1_black',
            'p1_blue',
            'p1_green',
            'p1_red',
            'p1_white',
            'p1_gold',
            'cpu_points',
            'p1_points',
            'take_pay_gems',
            'take_card',
            'reserve_card'
            ]
 
for var in var_list:
    if var not in st.session_state:
        if var == 'turn':
            st.session_state[var] = 1
        elif var in ['p1_reserve_deck', 'p1_deck', 'cpu_deck', 'cpu_reserve_deck']:
            st.session_state[var] = []
        elif var in ['cpu_points', 'p1_points']:
            st.session_state[var] = 0
        else:
            st.session_state[var] = ''
 
# colour dictionary
if 'colour_dict' not in st.session_state:
    st.session_state['colour_dict'] = {'bla':'black',
                                       'blu':'blue',
                                       'gre':'green',
                                       'red':'red',
                                       'whi':'white',
                                       'gol':'gold'}

# List of cards
if 'card_serials' not in st.session_state:
    st.session_state['card_serials'] = ['bla1002020',
                    'bla1002100',
                    'bla1003000',
                    'bla1011110',
                    'bla1020120',
                    'bla1021110',
                    'bla1040001',
                    'bla1101300',
                    'blu1000401',
                    'blu1002210',
                    'blu1101110',
                    'blu1101210',
                    'blu1200010',
                    'blu1202000',
                    'blu1300000',
                    'blu1013100',
                    'gre1000300',
                    'gre1010020',
                    'gre1020200',
                    'gre1031010',
                    'gre1110110',
                    'gre1210110',
                    'gre1210200',
                    'gre1400001',
                    'red1000030',
                    'red1000041',
                    'red1000220',
                    'red1021000',
                    'red1111010',
                    'red1111020',
                    'red1201020',
                    'red1300110',
                    'whi1004001',
                    'whi1030000',
                    'whi1100200',
                    'whi1110030',
                    'whi1111100',
                    'whi1112100',
                    'whi1122000',
                    'whi1220000']
    

if 'obj_serials' not in st.session_state:
    st.session_state['obj_serials'] = ['obj004403',
                   'obj033033',
                   'obj040043',
                   'obj044003',
                   'obj300333',
                   'obj303303',
                   'obj330033',
                   'obj400043',
                   'obj400403'
                   ]
    
# Initialise card slots
if 'slots' not in st.session_state:
    st.session_state['slots'] = ['card_1_1',
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
             'card_3_4']

# Initialise main deck
if 'main_deck' not in st.session_state:
    st.session_state['main_deck'] = []
    for serial in st.session_state['card_serials']:
        st.session_state['main_deck'] = st.session_state['main_deck'] + [serial]

# Initialise gem supply:

if 'gem_supply' not in st.session_state:
    st.session_state['gem_supply'] = {'black':6,
                                      'blue':6,
                                      'green':6,
                                      'white':6,
                                      'red':6,
                                      'gold':6
                                      }        

# Initialise cpu_gems and p1_gems
for gem in ['black', 'blue', 'green', 'red', 'white', 'gold']:
    if st.session_state['cpu_' + gem] =='':
        st.session_state['cpu_' + gem] = 0
    if st.session_state['p1_' + gem] =='':
        st.session_state['p1_' + gem] = 0

    
# Initialise cards_img_dict
if 'card_img_dict' not in st.session_state:
    st.session_state['card_img_dict'] = {'':"cards/splendor.jpg"}
    for card in st.session_state['card_serials']:
        st.session_state['card_img_dict'][card] = "cards/" + card + ".jpg"
        
    for key in st.session_state['card_img_dict'].keys():
        st.session_state['card_img_dict'][key] = ImageOps.exif_transpose(Image.open(st.session_state['card_img_dict'][key]))

# Initialise obj_img_dict
if 'obj_img_dict' not in st.session_state:
    st.session_state['obj_img_dict'] = {'':'cards/objective_cards/splendor.jpg'}
    for obj in st.session_state['obj_serials']:
        st.session_state['obj_img_dict'][obj] = "cards/objective_cards/" + obj + ".jpg"
        
    for key in st.session_state['obj_img_dict'].keys():
        st.session_state['obj_img_dict'][key] = ImageOps.exif_transpose(Image.open(st.session_state['obj_img_dict'][key]))

# confirm button
def confirm_button():
    
    # add drawn cards to tableau
    #for card in st.session_state['slots']:
    #    st.session_state['tableau_deck'] = st.session_state['tableau_deck'] + [st.session_state[card]]
        
    st.session_state['setup_complete'] = 'complete'
        
    # remove drawn cards from deck
    st.session_state['main_deck'] = [card for card in st.session_state['main_deck'] if card not in [st.session_state[slot] for slot in st.session_state['slots']]] #st.session_state['tableau_deck']]
         

# Initial set up interface 
st.write("Open the toggle to set up initial card tableau. Click Confirm setup when done")
if st.toggle("Game setup") and st.session_state['setup_complete']=='': 
    st.write("Please enter cards in colour-level-cost-points format:\n\n bla/blu/gre/red/whi for colour\n\n a 1 digit number for level\n\n a 5 digit number for the cost for the respective colours\n\n a 1 digit number for the points\n\n e.g. blu1333001\n\n Omit level for objective cards")
    
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
    obj_slot_1.image(st.session_state['obj_img_dict'][st.session_state['obj_1']])
    
with obj_tableau[1]:
    obj_slot_2 = st.empty()
    obj_slot_2.image(st.session_state['obj_img_dict'][st.session_state['obj_2']])
    
with obj_tableau[2]:
    obj_slot_3 = st.empty()
    obj_slot_3.image(st.session_state['obj_img_dict'][st.session_state['obj_3']])
    
tableau = st.columns(4)

with tableau[0]:
    slot_1_1 = st.empty()
    slot_1_1.image(st.session_state['card_img_dict'][st.session_state['card_1_1']])
    
    slot_2_1 = st.empty()
    slot_2_1.image(st.session_state['card_img_dict'][st.session_state['card_2_1']])
    
    slot_3_1 = st.empty()
    slot_3_1.image(st.session_state['card_img_dict'][st.session_state['card_3_1']])
   
with tableau[1]:
    slot_1_2 = st.empty()
    slot_1_2.image(st.session_state['card_img_dict'][st.session_state['card_1_2']])
    
    slot_2_2 = st.empty()
    slot_2_2.image(st.session_state['card_img_dict'][st.session_state['card_2_2']])
    
    slot_3_2 = st.empty()
    slot_3_2.image(st.session_state['card_img_dict'][st.session_state['card_3_2']])
    
with tableau[2]:
    slot_1_3 = st.empty()
    slot_1_3.image(st.session_state['card_img_dict'][st.session_state['card_1_3']])
    
    slot_2_3 = st.empty()
    slot_2_3.image(st.session_state['card_img_dict'][st.session_state['card_2_3']])
    
    slot_3_3 = st.empty()
    slot_3_3.image(st.session_state['card_img_dict'][st.session_state['card_3_3']])
    
with tableau[3]:
    slot_1_4 = st.empty()
    slot_1_4.image(st.session_state['card_img_dict'][st.session_state['card_1_4']])
    
    slot_2_4 = st.empty()
    slot_2_4.image(st.session_state['card_img_dict'][st.session_state['card_2_4']])
    
    slot_3_4 = st.empty()
    slot_3_4.image(st.session_state['card_img_dict'][st.session_state['card_3_4']])

### P1 MOVES
st.subheader("Player Actions")
# Take gems

def take_pay_gem(player, choice, coeff):
    
    gems = int(len(choice)/4)
    
    for gem in range(gems):
        
        colour = choice[4*gem:4*gem+3]
        number = int(choice[4*gem + 3])
        
        st.session_state[player + st.session_state['colour_dict'][colour]] += number * coeff
        st.session_state['gem_supply'][st.session_state['colour_dict'][colour]] -= number * coeff
    
    
st.subheader("Take or Pay Gems")    
st.write("Enter gems in colour-number format e.g. blu2bla3 for 2 blue and 3 black")
st.session_state['take_pay_gems'] = st.text_input("Gems")    

# Take / pay buttons

take_pay = st.columns(2)

with take_pay[0]:
    st.button("Take gems",
              on_click=take_pay_gem,
              args = ('p1_', st.session_state['take_pay_gems'], 1))
    
with take_pay[1]:
    st.button("Pay gems",
              on_click=take_pay_gem,
              args = ('p1_', st.session_state['take_pay_gems'], -1))

# Take a card
st.subheader("Take a Card")

def take_card(deck, slot):
    
    # add card to player/cpu deck
    st.session_state[deck] = st.session_state[deck] + [st.session_state[slot]]
    
    # remove card from tableau
    st.session_state[slot] = ''

st.write("Enter card slot to take from in card_level_column format e.g. card_3_4")
st.session_state['take_card'] = st.text_input("Card Slot to Take From")

st.button("Take card",
          on_click=take_card,
          args = ('p1_deck', st.session_state['take_card']))



# Reserve card    

st.write("Enter card slot to reserve from in card_level_column format e.g. card_3_4")
st.session_state['reserve_card'] = st.text_input("Card Slot to Reserve From")

st.button("Reserve card",
          on_click=take_card,
          args = ('p1_reserve_deck', st.session_state['reserve_card']))

st.subheader("Draw card from deck")

# Buy reserved card


#def xyz():
#    slot_1_1.empty()
#    st.session_state['card_1_1'] = '1'
#    slot_1_1.image(cards_dict[st.session_state['card_1_1']])
    
#st.button("change 1,1 pic to splendor", on_click=xyz)
###############

# Remaining cards
st.session_state['level_1'] = [card for card in st.session_state['main_deck'] if card[3] == '1']
st.session_state['level_2'] = [card for card in st.session_state['main_deck'] if card[3] == '2']
st.session_state['level_3'] = [card for card in st.session_state['main_deck'] if card[3] == '3']

# gem supply
for gem in ['black', 'blue', 'green', 'red', 'white', 'gold']:
    st.session_state[gem] = st.session_state['gem_supply'][gem]

st.subheader("Cards")

st.write("Deck contains: " + str(len((st.session_state['main_deck']))))
st.write("Level 1 cards remaining: " + str(len(st.session_state['level_1'])))
st.write("Level 2 cards remaining: " + str(len(st.session_state['level_2'])))
st.write("Level 3 cards remaining: " + str(len(st.session_state['level_3'])))

st.subheader("Gems")

resources = st.columns(3)

with resources[0]:
    for gem in ['black', 'blue', 'green', 'red', 'white', 'gold']:  
        st.write(gem + " gems remaining: " + str(st.session_state[gem]))

with resources[1]:    
    for gem in ['black', 'blue', 'green', 'red', 'white', 'gold']:
        st.write("CPU " + gem + " gems: " + str(st.session_state["cpu_" + gem]))

with resources[2]:    
    for gem in ['black', 'blue', 'green', 'red', 'white', 'gold']:  
        st.write("P1 " + gem + " gems: " + str(st.session_state["p1_" + gem]))


st.write("Player 1 deck")
st.session_state['p1_deck']

st.write("Player 1 reserve deck")
st.session_state['p1_reserve_deck']
st.write("session state:card_1_2 value")
st.session_state['card_1_2']
st.write("session st reserve card")
st.session_state['reserve_card']
    
    