# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:04:32 2024

@author: jd_se
"""
from PIL import Image, ImageOps

# List of cards
card_serials = ['bla1002020',
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

obj_serials = ['obj004403',
               'obj033033',
               'obj040043',
               'obj044003',
               'obj300333',
               'obj303303',
               'obj330033',
               'obj400043',
               'obj400403'
               ]


slots = ['card_1_1',
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

# confirm button
def confirm_button():
    # create deck of cards (dictionary)
    for serial in card_serials:
        
        # add to deck
        st.session_state['deck'] = st.session_state['deck'] + [serial]
    
    st.session_state['setup_complete'] = 'complete'
    
    # add drawn cards to tableau
    for card in slots:
        st.session_state['tableau_deck'] = st.session_state['tableau_deck'] + [st.session_state[card]]
        
    # remove drawn cards from deck
    st.session_state['deck'] = [card for card in st.session_state['deck'] if card not in st.session_state['tableau_deck']]
    
# intialise cards_dict
cards_dict = {'':'cards/splendor.jpg'}

for card in card_serials:
    cards_dict[card] = "cards/" + card + ".jpg"
    
for key in cards_dict.keys():
    cards_dict[key] = ImageOps.exif_transpose(Image.open(cards_dict[key]))

# initialise objs_dict
objs_dict = {'':'cards/splendor.jpg'}

for obj in obj_serials:
    objs_dict[obj] = "cards/objective_cards/" + obj + ".jpg"

for key in objs_dict.keys():
    objs_dict[key] = ImageOps.exif_transpose(Image.open(objs_dict[key]))
