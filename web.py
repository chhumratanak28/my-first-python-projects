import streamlit as st
st.title("Ratanak's python tip calculator")
bill = st.number_input("what was the total bill? ($)", min_value=0.0 , step=1.0)
tip_percent =  st.slider("What percentage tip would you like to give? ", 0,30,50)
people = st.number_input("How many people are splitting the bill?", min_value=1, value=1)
tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
per_person = total_bill / people
st.subheader(f"tip amount: ${tip_amount:.2f}")
st.subheader(f"Total to pay: ${total_bill:.2f}")
st.success(f"Each person pays: ${per_person:.2f}")
if st.button("Celebrate! 🔥"):
    st.balloons()