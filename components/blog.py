import streamlit as st

def app():
    st.title("R&R Telehealth Blog")
    st.write("""
    Welcome to our blog! Here, we share the latest news, health tips, and insights on telehealth and healthcare trends.
    """)

    # Articles Section
    st.write("**Recent Posts:**")

    # Article 1
    if st.button("The Benefits of Telehealth in Rural Areas"):
        st.image("images/blog1.webp", width=500)
        st.write("""
        **The Benefits of Telehealth in Rural Areas**

        Telehealth has been a game-changer for rural communities, providing access to healthcare services that were previously unavailable or difficult to reach. With telehealth, patients in rural areas can now consult with specialists, receive timely care, and manage chronic conditions without the need to travel long distances.

        Learn more about how telehealth is transforming healthcare in rural areas and improving patient outcomes.
        """)

    # Article 2
    if st.button("How to Manage Chronic Conditions with Telehealth"):
        st.image("images/blog2.jpg", width=500)
        st.write("""
        **How to Manage Chronic Conditions with Telehealth**

        Managing chronic conditions such as diabetes, hypertension, and asthma can be challenging, especially for patients who have difficulty accessing regular in-person care. Telehealth offers a convenient and effective solution, allowing patients to monitor their conditions, consult with healthcare providers, and receive personalized care plans from the comfort of their homes.

        Discover the ways telehealth is helping patients take control of their health and manage chronic conditions effectively.
        """)

    # Article 3
    if st.button("Understanding the Role of AI in Healthcare"):
        st.image("images/blog3.jpg", width=500)
        st.write("""
        **Understanding the Role of AI in Healthcare**

        Artificial Intelligence (AI) is revolutionizing the healthcare industry by improving diagnostics, enhancing patient care, and streamlining administrative processes. From AI-driven imaging analysis to predictive analytics for personalized treatment plans, the possibilities are endless.

        Explore how AI is being integrated into healthcare systems and the potential it holds for the future of medicine.
        """)

    st.write("**Stay tuned for more updates and expert advice on health and wellness.**")

    # Separator
    st.markdown("---")
    
    # Recent Camps Section
    st.header("Recent Diabetes Camps")
    st.write("We regularly organize diabetes camps to help patients manage their condition and learn about the latest in diabetes care.")

    if st.button("View Recent Diabetes Camps"):
        st.image("images/blog4.jpg", width=500)
        st.write("""
        **Recent Diabetes Camps**

        Our recent diabetes camps have been a great success, offering patients comprehensive care and education. From blood sugar monitoring to diet counseling, these camps are designed to empower patients with the knowledge and tools they need to manage their diabetes effectively.

        **Ask your Doctor to learn more about upcoming camps and how you can participate.**
        """)

    # Doctors' Advice Section
    st.header("Doctors' Advice")
    st.write("Our expert doctors share their advice on managing health and wellness.")

    if st.button("Read Doctors' Advice"):
        st.image("images/doctor7.jpg", width=500)
        st.write("""
        **Doctors' Advice for Patients**

        Our doctors emphasize the importance of regular check-ups, a balanced diet, and staying active. Whether you're managing a chronic condition or just looking to maintain a healthy lifestyle, our team is here to provide you with the guidance you need.

        
        """)

if __name__ == "__main__":
    app()
