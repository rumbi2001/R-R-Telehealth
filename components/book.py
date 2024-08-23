import streamlit as st

def app():
    st.title("Book an Appointment")
    st.write("""
    Use the form below to book an appointment with one of our healthcare professionals. 
    You can choose a date and time that suits you.
    """)
    
    # Placeholder form for booking
    with st.form("appointment_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        date = st.date_input("Preferred Date")
        time = st.time_input("Preferred Time")
        symptoms = st.text_area("Describe your symptoms")

        submitted = st.form_submit_button("Book Appointment")
        if submitted:
            st.success(f"Appointment booked for {date} at {time} with {name}.")
