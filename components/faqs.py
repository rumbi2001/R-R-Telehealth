import streamlit as st

def app():
    st.title("Frequently Asked Questions (FAQs)")

    st.image("images/faqs1.webp", width=250)

    st.write("Click on a question to reveal the answer:")

    # FAQ 1: What is telehealth?
    if st.button("**Q: What is telehealth?**"):
        st.write("""
        **A:** Telehealth refers to the use of digital information and communication technologies, such as computers and mobile devices, to access healthcare services remotely.
        """)

    # FAQ 2: How do I book an appointment?
    if st.button("**Q: How do I book an appointment?**"):
        st.write("""
        **A:** You can book an appointment through our "Book an Appointment" page by filling out the form with your details.
        """)

    # FAQ 3: Is my information secure?
    if st.button("**Q: Is my information secure?**"):
        st.write("""
        **A:** Yes, we use industry-standard security measures to ensure your personal and medical information is kept confidential and secure.
        """)

    # FAQ 4: Can I get a prescription refill online?
    if st.button("**Q: Can I get a prescription refill online?**"):
        st.write("""
        **A:** Yes, after a consultation, our doctors can prescribe medication and have it sent directly to your pharmacy.
        """)

if __name__ == "__main__":
    app()
