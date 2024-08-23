import streamlit as st
import random

def app():
    st.title("Patient Portal")
    st.write("""
    Welcome to the Patient Portal. Here, you can communicate with your healthcare provider!!!
    """)

    st.subheader("Meet Our Doctors")

    doctors = [
        {"name": "Dr. John Doe", "specialty": "Cardiologist", "image": "images/doctor1.png"},
        {"name": "Dr. Rumbidzai Smith", "specialty": "Endocrinologist", "image": "images/doctor2.jpg"},
        {"name": "Dr. Richard Roe", "specialty": "Gastroenterologist", "image": "images/doctor3.png"},
        {"name": "Dr. Tshepang Davis", "specialty": "Neurologist", "image": "images/doctor4.jpg"},
        {"name": "Dr. Michael Brown", "specialty": "Orthopedic Surgeon", "image": "images/doctor5.webp"},
        {"name": "Dr. Nyasha Mac", "specialty": "Pediatrician", "image": "images/doctor6.png"},
    ]

    cols = st.columns(3)
    
    selected_doctor = None  # Track which doctor is selected for the call
    
    for i, doctor in enumerate(doctors):
        col = cols[i % 3]
        with col:
            # Display doctor information in a card
            with st.expander(f"{doctor['name']} - {doctor['specialty']}"):
                st.image(doctor["image"], use_column_width=True)
                available = random.choice([True, False])
                if available:
                    status = "Available"
                else:
                    status = "Offline"
                
                st.write(f"Status: **{status}**")
                
                if available:
                    if st.button(f"Call {doctor['name']}", key=f"call_{i}"):
                        selected_doctor = doctor  # Store the selected doctor

    if selected_doctor:
        st.sidebar.title("Chat with Your Doctor")
        st.sidebar.image(selected_doctor["image"], use_column_width=True)
        st.sidebar.markdown(f"### {selected_doctor['name']} - {selected_doctor['specialty']}")
        st.sidebar.write("**Status: Available**")
        st.sidebar.markdown("### Video Call Interface")
        st.sidebar.write("This is a simulated video call screen.")
        st.sidebar.text_area("Chat", value="You: Hi Doctor\nDoctor: Hello, how can I assist you today?", height=200)
        st.sidebar.button("End Call", key="end_call")

if __name__ == "__main__":
    app()
