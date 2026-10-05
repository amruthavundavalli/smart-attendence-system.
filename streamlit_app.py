import streamlit as st

st.set_page_config(
    page_title="Smart Attendance System",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Smart Attendance System")
st.success("Streamlit website is working!")

st.sidebar.title("Menu")

page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "Students",
        "Attendance",
        "Reports"
    ]
)

if page == "Dashboard":
    st.header("Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Students", 0)
    col2.metric("Present Today", 0)
    col3.metric("Attendance Rate", "0%")

elif page == "Students":
    st.header("Students")
    st.info("Student management will be added next.")

elif page == "Attendance":
    st.header("Attendance")
    st.info("Attendance system will be added next.")

elif page == "Reports":
    st.header("Reports")
    st.info("Reports will be added next.")