import streamlit as st

def app():
    # Header section with logo and title
    col1, col2 = st.columns([1, 6])  # Adjust the ratio if needed
    
    with col1:
        st.image("images/logo1.jpg", width=120)  # Logo in the first column
    
    with col2:
        st.title("About Us")  # Title in the second column
    
    # Section 1: Image next to "Our aim" text
    col3, col4 = st.columns([3, 5])
    
    with col3:
        st.image("images/about1.jpg")  # Image for "Our aim"
    
    with col4:
        st.write("""
        Our aim is to revolutionize healthcare by leveraging AI and telemedicine to improve the management, 
        analysis, and delivery of healthcare services. By integrating AI-driven document intelligence, data management
        systems, and telemedicine capabilities, we seek to enhance patient outcomes, reduce errors, and increase 
        the accessibility and efficiency of healthcare delivery. Our solution aligns with SDG 3, aiming to ensure
        healthy lives and promote well-being for all.
        """)
    
    # Section 2: Image next to "R&R Telehealth" text
    col5, col6 = st.columns([3, 5])
    
    with col5:
        st.image("images/about2.webp")  # Image for "R&R Telehealth"
    
    with col6:
        st.write("""
        **R&R Telehealth** is committed to providing quality healthcare through accessible and innovative telehealth solutions.
        Our mission is to bridge the gap between healthcare providers and patients, ensuring that everyone has access to medical care, 
        regardless of their location. With our team of dedicated professionals and advanced technology, we bring healthcare to you.
        """)
    
    # Add a separator
    st.markdown("---")
    
    # Section 3: YouTube video with custom size
    st.header("Learn more about Telemedicine")
    st.markdown("""
        <iframe width="700" height="405" src="https://www.youtube.com/embed/C6cr__DNnnU?si=pSOZjSHvQOsPm2uE" 
        title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; 
        gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
