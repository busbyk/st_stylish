import streamlit as st
import streamlit.components.v1 as components

from st_stylish.helpers import set_last_component_full_page

st.set_page_config(layout='wide')
set_last_component_full_page()

with st.sidebar:
  st.write('Sidebar Content')

components.iframe('https://jupyter.org/try-jupyter/lab/')