import streamlit as st

def creators():
    st.header("Website Creators")

    # Create two columns
    col1, col2 = st.columns(2)

    # Unicode characters for email and phone symbols
    email_icon = "📧"
    phone_icon = "☎️"
    # Custom CSS for changing font
    custom_css = """
        <style>
            .custom-font {
                font-family: 'Arial', sans-serif;
                font-size: 16px;
                color: #333; /* Set the text color */
            }
        </style>
    """

    # Apply the custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    # Creator 1
    with col1:
        # st.subheader("Creator 1")
        st.image("harsha.jpg", width=270, caption="Creator 1")
        st.markdown("Name: D Veera Harsha Vardhan Reddy", unsafe_allow_html=True)
        st.markdown(f"{email_icon} : dveeraharshavardhanreddy@gmail.com", unsafe_allow_html=True)
        st.markdown(f"{phone_icon} : +91 9014831254", unsafe_allow_html=True)

    # Creator 2
    with col2:
        # st.subheader("Creator 2")
        st.image("sumanth.jpg", width=270, caption="Creator 2")
        st.markdown("Name: V Sai Sumanth", unsafe_allow_html=True)
        st.markdown(f"{email_icon} : vsaisumanth15@gmail.com", unsafe_allow_html=True)
        st.markdown(f"{phone_icon} : +91 8688154917", unsafe_allow_html=True)
        
        
        
