import streamlit as st
from .helpers import set_appview_padding, set_main_container_height_width, set_vertical_block_gap, set_last_component_height_width


class StyleInjector:
  def __init__(self):
    self.markdown_injections_count = 0
    self.st_component_injections_count = 0

  def __enter__(self):
    return self

  def __exit__(self, type, value, traceback):
    print(f'__exit__: current markdown_injections_count = {self.markdown_injections_count}')

    if type is not None and value is not None and traceback is not None:
      print(f'type: {type}, value: {value}, traceback: {traceback}')
      return False

    return True


  def increment_markdown_injections_count(self, count = 1):
    self.markdown_injections_count += count

  def increment_st_component_injections_count(self, count = 1):
    self.st_component_injections_count += count


  def set_appview_padding(self, *args, **kwargs):
    self.increment_markdown_injections_count()
    set_appview_padding(*args, **kwargs)

    
  def set_main_container_height_width(self, *args, **kwargs):
    self.increment_markdown_injections_count()
    set_main_container_height_width(*args, **kwargs)


  def set_vertical_block_gap(self, *args, **kwargs):
    self.increment_markdown_injections_count()
    set_vertical_block_gap(*args, **kwargs)


  """
  Sets the height and width of the last element container in any
  vertical block inside the main block container.
  Element containers are the html div tags that house Streamlit widgets.

  Parameters
  ----------
  height : str
      Height of the main block container in any valid CSS
      (i.e. px, em, rem, %, vh/vw)
  width : str
      Width of the main block container in any valid CSS
      (i.e. px, em, rem, %, vh/vw)

  Returns
  -------
  Return value of st.markdown
  """
  def set_n_component_height_width(self, idx, height, width):
    self.increment_markdown_injections_count()
    st.markdown(f"""
        <style>
            .block-container > div > div[data-testid="stVerticalBlock"] {{
                width: {width} !important;
            }}
            
            .block-container > div > div[data-testid="stVerticalBlock"] > div.element-container:nth-of-type({ idx + self.markdown_injections_count }) {{
                height: {height} !important;
                width: {width} !important;
            }}

            .block-container > div > div[data-testid="stVerticalBlock"] > div.element-container:nth-of-type({ idx + self.markdown_injections_count }) > * {{
                height: 100%;
                width: 100%;
                position: absolute;
                top: 0;
                left: 0;
                border: 0;
            }}
        </style> 
        """, unsafe_allow_html=True)