import streamlit as st
import configparser
from crud_app_jrb.__main__ import show_all
from crud_app_jrb.db_interact import connect, get_cfg
from dotenv import load_dotenv
import os

@st.cache_resource
def load_database():
    config = get_cfg()
    connection = connect(config)
    return connection

conexion = load_database()

st.title("CRUD APP")

st.subheader("Functionalities")

show, create, search = st.tabs(["My Table", "Create", "Search"])

with show:
    st.dataframe(show_all())


with search:
    song = st.text_input("Song name: ")
    album = st.text_input("Album name: ")
    artist = st.text_input("Artist name: ")
    genre = st.text_input("Genre: ")
