import streamlit as st

def app():
    st.title("Contact Us")
    st.write("""
    We’d love to hear from you! If you have any questions or need assistance, please reach out to us:
    
    - **Phone:** +267 123 4567
    - **Email:** support@rrtelehealth.com
    - **Address:** Plot 1234, Gaborone, Botswana
    
    Alternatively, you can use the form below to send us a message:
    """)
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thank you! Your message has been sent.")
