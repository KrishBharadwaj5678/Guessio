import streamlit as st
import random as r

st.set_page_config(page_title="Guessio",
                   page_icon="icon.png",
                   menu_items={"About": """Enjoy the thrill of guessing with Guessio! Pick a number between 1 and 100 and see how soon you can guess the right one. Simple gameplay, endless fun—start guessing now!"""})

st.write("<h2 style=color:#FF8343;>Conquer the Number Challenge</h2>",
         unsafe_allow_html=True)

number = st.number_input("Guess a Number Between 1 and 100",
                         min_value=1,
                         max_value=100)

if "loadstate" not in st.session_state:
         st.session_state.loadstate = False

if "answer" not in st.session_state:
         st.session_state.answer = r.randrange(1, 100+1)

btn = st.button("Check")
restart=st.button("Restart")

if restart:
     st.session_state.loadstate = False
     st.session_state.answer = r.randrange(1, 100+1)

if btn or st.session_state.loadstate:
         st.session_state.loadstate = True

         if (number == st.session_state.answer):
           
                  st.write(
                      "<h2 style=color:lightgreen;>You Did It! Congratulations!</h2>",
                      unsafe_allow_html=True)
                  
                  st.balloons()

         elif (number > st.session_state.answer):
                  st.write(
                      "<h2 style=color:#FF4C4C;>Try Again! You guessed too High</h2>",
                      unsafe_allow_html=True)

         else:
                  st.write(
                      "<h2 style=color:orange;>Try Again! You guessed too Small</h2>",
                      unsafe_allow_html=True)
