import streamlit as st
import streamlit.components.v1 as components

# This is the height of the top nav, content will be hidden 
# if we don't include at least this much padding
MIN_PADDING_TOP=3

"""Set padding of the app view main block container (main app area) in Streamlit

Parameters
----------
top : int
    Padding in rem to be applied to the top of the block container,
    set as the value for right, bottom, left if those are omitted
right : int
    Padding in rem to be applied to the right of the block container,
    set as the value for bottom, left if those are omitted
bottom : int
    Padding in rem to be applied to the bottom of the block container
left : int
    Padding in rem to be applied to the left of the block container

Returns
-------
Return value of st.markdown

"""
def set_appview_padding(top = 0, right = None, bottom = None, left = None):
    if top is not None and right is None and bottom is None and left is None:
        right = top
        bottom = top
        left = top
    
    if right is not None and bottom is None and left is None:
        bottom = right
        left = right

    st.markdown(f"""
        <style>
            .appview-container .main .block-container,
            .reportview-container .main .block-container {{
                padding-top: {MIN_PADDING_TOP + top}rem;
                padding-right: {right}rem;
                padding-left: {bottom}rem;
                padding-bottom: {left}rem;
            }} 
        </style> 
        """, unsafe_allow_html=True)


def set_main_container_height_width(height, width):
    st.markdown(f"""
        <style>
            .appview-container .main .block-container,
            .reportview-container .main .block-container {{
                height: {height} !important;
                width: {width} !important;
            }} 
            
            .appview-container .main .block-container > div,
            .reportview-container .main .block-container > div {{
                height: {height} !important;
                width: {width} !important;
            }}
        </style> 
        """, unsafe_allow_html=True)


def set_vertical_block_gap(gap):
    st.markdown(f"""
        <style>
            .block-container > div > div[data-testid="stVerticalBlock"] {{
                gap: {gap};
            }}
        </style> 
        """, unsafe_allow_html=True)


def set_component_height_width(height, width):
    st.markdown(f"""
        <style>
            .block-container > div > div[data-testid="stVerticalBlock"] {{
                width: {width} !important;
            }}
            
            .block-container > div > div[data-testid="stVerticalBlock"] > div.element-container:last-of-type {{
                height: {height} !important;
                width: {width} !important;
            }}

            .block-container > div > div[data-testid="stVerticalBlock"] > div.element-container:last-of-type > * {{
                height: 100%;
                width: 100%;
                position: absolute;
                top: 0;
                left: 0;
                border: 0;
            }}
        </style> 
        """, unsafe_allow_html=True)


def full_page_iframe(**args):
    set_appview_padding(0)
    set_main_container_height_width()
    set_component_height_width()


def inject_local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style class="kb">{f.read()}</style>', unsafe_allow_html=True)


def inject_local_script(file_name):
    with open(file_name) as f:
        components.html(f'<script>{f.read()}</script>', height=0)