import streamlit as st

st.title("🏝️ Treasure Island 🏝️")



st.write("Welcome to *Treasure Island*.")
st.subheader("Your mission is to find the treasure. 🏆")

choice1 = st.selectbox('You\'re at a crossroad 🛤️, where do you want to go? Type "left" or "right".', ['left', 'right'])
if choice1 == 'left':
    choice2 = st.selectbox('You\'ve come to a lake 🌊. There is an island in the middle of the lake. Type "wait" to wait for a boat 🚤 or "swim" to swim 🏊 across.', ['wait', 'swim'])
    if choice2 == 'wait':
        choice3 = st.selectbox("You arrive at the island unharmed 🏝️. There is a house with 3 doors: one red 🚪🔴, one yellow 🚪🟡, and one blue 🚪🔵. Which colour do you choose?", ['red', 'yellow', 'blue'])
        if choice3 == "red":
            st.error("🔥 It's a room full of fire. Game Over. 🔥")
        elif choice3 == "yellow":
            st.success("🎉 You found the treasure! You Win! 🎉")
        elif choice3 == "blue":
            st.error("🧟 You enter a room of beasts. Game Over. 🧟")
        else:
            st.error("❌ You chose a door that doesn't exist. Game Over. ❌")
    else:
        st.error("🐟 You got attacked by an angry trout. Game Over. 🐟")
else:
    st.error("🕳️ You fell into a hole. Game Over. 🕳️")
