import streamlit as st

from st_stylish.StyleInjector import StyleInjector

st.set_page_config(layout='wide')

with StyleInjector() as injector:
  injector.set_appview_padding(0)
  injector.set_main_container_height_width(height="100%", width="100%")
  injector.set_vertical_block_gap(0)

  code = '''def hello():
     print("First component")'''
  st.code(code, language='python')
  injector.set_n_component_height_width(0, height="50%", width="100%")
  st.write('Second component')
  injector.set_n_component_height_width(1, height="50%", width="100%")
  st.write('Third component, unaffected/unstyled')
