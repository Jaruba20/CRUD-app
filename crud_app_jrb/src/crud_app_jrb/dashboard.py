import streamlit as st
import configparser
from crud_app_jrb.__main__ import show_all, set_table
#from crud_app_jrb.db_interact import connect, get_cfg
from dotenv import load_dotenv
import os
from crud_app_jrb.Connection import Connection

@st.cache_resource
def connect(cfg = os.getenv("CRUD_APP_CONFIG_FILE", default=".cfg")):
    connection = Connection(cfg)



st.title("CRUD APP")

st.subheader("Functionalities")

show_tab, create_tab, search_tab = st.tabs(["My Table", "Create", "Search"])


with show_tab:
    st.dataframe(show_all())


with search_tab:
    song = st.text_input("Song name: ")
    album = st.text_input("Album name: ")
    artist = st.text_input("Artist name: ")
    genre = st.text_input("Genre: ")
