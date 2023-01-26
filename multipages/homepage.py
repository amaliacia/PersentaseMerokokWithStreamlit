import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title="MENU",
    options=["Home", "Persentase", "About"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    orientation="horizontal",
    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
    )

if selected == "Home":
    st.title("Welcome to Our Page")
if selected == "Persentase":
    st.title("Berikut Data Persentase Perokok Di Indonesia")
if selected == "About":
    st.title("Data Pembuat")
    st.subheader("Amalia Suciati")
    st.text("NIM : 21102069")
    st.text("Kelas : IF 09 M")

    