import streamlit as st

def app():
    # Title of the section
    st.title("Our Services")
    
    # Custom CSS for animations
    st.markdown("""
        <style>
        .fade-in {
            animation: fadeIn 3s ease-in-out forwards;
            opacity: 0;
        }
        
        .slide-in {
            animation: slideIn 2s ease-out forwards;
            transform: translateX(-100%);
        }
        
        .pulse {
            animation: pulse 2s infinite;
        }
        
        @keyframes fadeIn {
            to {
                opacity: 1;
            }
        }
        
        @keyframes slideIn {
            to {
                transform: translateX(0);
            }
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        .service {
            font-size: 20px;
            margin-top: 20px;
            padding: 10px;
            border-left: 5px solid #4CAF50;
        }

        .virtual-consultations {
            color: #4CAF50;
        }

        .prescription-refills {
            color: #2196F3;
        }

        .specialist-referrals {
            color: #FF9800;
        }

        .chronic-disease-management {
            color: #9C27B0;
        }

        .health-monitoring {
            color: #F44336;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Services with animations
    st.markdown('<div class="service fade-in virtual-consultations">Virtual Consultations: Connect with a doctor from the comfort of your home.</div>', unsafe_allow_html=True)
    st.markdown('<div class="service slide-in prescription-refills">Prescription Refills: Get your prescriptions refilled without needing to visit a clinic.</div>', unsafe_allow_html=True)
    st.markdown('<div class="service fade-in specialist-referrals">Specialist Referrals: If needed, we can refer you to specialists for further treatment.</div>', unsafe_allow_html=True)
    st.markdown('<div class="service pulse chronic-disease-management">Chronic Disease Management: Ongoing care and monitoring for chronic conditions.</div>', unsafe_allow_html=True)
    st.markdown('<div class="service slide-in health-monitoring">Health Monitoring: Remote monitoring of vital signs and health data.</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
