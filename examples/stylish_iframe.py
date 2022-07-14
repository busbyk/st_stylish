import streamlit as st
import streamlit.components.v1 as components

from st_stylish.iframe import stylish_iframe
from st_stylish.helpers import set_appview_padding, set_main_container_height_width, set_vertical_block_gap, set_component_height_width

st.set_page_config(layout='wide')
set_appview_padding(0)
set_main_container_height_width(height="100%", width="100%")
set_vertical_block_gap(0)
set_component_height_width(height="100%", width="100%")

with st.sidebar:
  st.write('Sidebar Content')

# components.iframe('https://jupyter.org/try-jupyter/lab/')
stylish_iframe('https://jupyter.org/try-jupyter/lab/')