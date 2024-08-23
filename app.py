import streamlit as st
from components import home, about, services, book, portal, faqs, contact, privacy_policy, terms, blog, careers

st.set_page_config(page_title="R&R Telehealth", layout="wide")

# A dictionary to store the pages
PAGES = {
    "Home": home,
    "About Us": about,
    "Services": services,
    "Book an Appointment": book,
    "Patient Portal": portal,
    "FAQs": faqs,
    "Contact Us": contact,
    "Privacy Policy": privacy_policy,
    "Terms of Service": terms,
    "Blog": blog,
    "Careers": careers,
}

# Sidebar for Navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", list(PAGES.keys()))

# Update the session state with the selected page
st.session_state.page = selected_page

# Load and display the selected page
def main():
    page_app = PAGES[st.session_state.page]
    page_app.app()

if __name__ == "__main__":
    main()
