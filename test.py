import streamlit as st
import streamlit.components.v1 as components

from helpers import set_appview_padding, set_main_container_height_width, set_vertical_block_gap, set_component_height_width
from iframe import stylish_iframe

st.set_page_config(layout='wide')
set_appview_padding(0)
set_main_container_height_width(height="100%", width="100%")
set_vertical_block_gap(0)
set_component_height_width(height="100%", width="100%")

with st.sidebar:
  st.write('sidebar')

components.iframe('https://jupyter.org/try-jupyter/lab/')
# stylish_iframe('https://jupyter.org/try-jupyter/lab/')
