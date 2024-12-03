import streamlit as st
import random

if 'select' not in st.session_state:
    st.session_state.select=0
def game_selection():
    if st.checkbox("user guessing",key="user"):
        st.session_state.select=1
        st.write("CLICK ONE MORE TIME")
    elif st.checkbox("machine guessing",key="machine"):
        st.session_state.select=2
        st.write("CLICK ONE MORE TIME")
    else:
        None
def guessing_game_by_user():
    if 'num_to_be_guessed' not in st.session_state:
        st.session_state.num_to_be_guessed = random.randrange(1, 100)
    if 'count' not in st.session_state:
        st.session_state.count = 1
    
    st.markdown("<h3 style='text-align:center; color:slateblue; font-weight:bold;'> GUESSING GAME</h3>", unsafe_allow_html=True)

    if st.session_state.count < 11:
        guessed_number = st.number_input(label='ENTER YOUR GUESSED NUMBER between 1 to 100:', min_value=1,max_value=100,key='num')
        if st.session_state.count == 1:
            st.write("YOU HAVE 10 CHANCES")
        else:
            None

        if guessed_number:
        
            if guessed_number > 100 or guessed_number < 1:
                st.write("INVALID INPUT")
            elif guessed_number == st.session_state.num_to_be_guessed:
                st.write("CONGRATULATIONS, YOU WIN!")
            else:
                st.write(f'ATTEMPT: {st.session_state["count"]}')
                st.write("SORRY, TRY AGAIN")
                st.session_state.count += 1
                if guessed_number < st.session_state['num_to_be_guessed']:
                    st.write("THE NUMBER TO BE GUESSED IS GREATER THAN YOUR INPUT NUMBER")
                elif guessed_number  >st.session_state['num_to_be_guessed']:
                    st.write("THE NUMBER TO BE GUESSED IS SMALLER THAN YOUR INPUT NUMBER")
                else:
                    None    
    else:
        st.write("SORRY, YOU FAILED. The number was:", st.session_state['num_to_be_guessed'])
        if st.button("Play Again"):
            st.stop()

def guessing_game_by_machine():
    low = 1
    high = 100
    attempts =10

    st.title("Number Guessing Game!")
    st.write("Think of a number between 1 and 100, and I'll try to guess it.")

    if 'attempt' not in st.session_state:
        st.session_state.attempt = 0
        st.session_state.low = low
        st.session_state.high = high

    if st.session_state.attempt < attempts:
        mid = (st.session_state.low + st.session_state.high)//2
        st.write(f"Is your number {mid}?")
        if st.checkbox('correct value',key="correct"):
           st.session_state.select=3
        if st.checkbox('high value',key="high"):
            st.session_state.select=4
        if st.checkbox('low value',key="low"):
            st.session_state.select=5
        if st.button('submit'):
            if  st.session_state.select==3:
                st.success(f"Yay! I guessed your number {mid} in {st.session_state.attempt + 1} attempts.")
                st.session_state.attempt = attempts  # End game
            
        
                
                if  st.session_state.select==4:
                    st.write("THE NUMBER TO BE GUESSED HIGHER THAN YOUR INPUT NUMBER")
                    st.session_state.high = mid - 1
                if  st.session_state.select==5:
                    st.write("THE NUMBER TO BE GUESSED IS SMALLER THAN YOUR INPUT NUMBER")
                    st.session_state.low = mid + 1
                else:
                    None    
            st.session_state.attempt += 1
            
    else:
        st.error("I couldn't guess your number within 10 attempts. Better luck next time!")



if st.session_state.select == 0:
    
    st.markdown("<h1 style='text-align:center; color:cyan;' >PORTFOLIO</h1>",unsafe_allow_html=True)
    st.header( "Hlo I'm Madhumitha Arunkumar")
    st.subheader("About Me:")
    st.write(""" I'm a B.Tech Artificial Inteligence and Datascience Programmer.And I'm currently doing UG first year
         at KGISL Institute of Technology. I have completed Jr. in English Typerwriting.
         Basically I'm a throwball player and I have reached District Level.And I'm a sports player  """)
    st.write("""If you have any doubt or queries you can contact me anytime 
    """)
    
    st.write( "ph: 044-2342-55")

    st.markdown("<h3 style='text-align:left; color:slateblue;'> WOULD YOU LIKE TO TRY MY GUESSING GAME</h3>", unsafe_allow_html=True)
    if st.checkbox("YES"):
        st.write(" CHOOSE A WAY YOU'D LIKE TO PLAY MY GUESSING GAME")
        game_selection()
    if st.button("no thanks"):
        None
    
else:
    if st.session_state.select == 1:
        guessing_game_by_user()
    elif st.session_state.select == 2:
        guessing_game_by_machine()
    else:
        None

