import streamlit as st
import streamlit.components.v1 as components

# This is the height of the top nav, content will be hidden 
# if we don't include at least this much padding
MIN_PADDING_TOP=3

"""
Set padding of the app view main block container (main app area) in Streamlit

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


"""
Sets the height and width of the main block container.
This is the html div tag that houses elements added to the page
via Streamlit widgets.

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


"""
Sets the CSS gap property of vertical blocks in the main block container.
Vertical blocks contain element containers (i.e. Streamlit widgets).
This essentially sets the padding between those vertical blocks. 
Additional vertical blocks can be added by using st.container for example.
This will apply to all vertical blocks.

Parameters
----------
gap : str or int
    Gap container in any valid CSS
    (i.e. px, em, rem, %, vh/vw)

Returns
-------
Return value of st.markdown

"""
def set_vertical_block_gap(gap):
    st.markdown(f"""
        <style>
            .block-container > div > div[data-testid="stVerticalBlock"] {{
                gap: {gap};
            }}
        </style> 
        """, unsafe_allow_html=True)


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
def set_last_component_height_width(height, width):
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


"""
Makes the last component in a vertical block in the main block container
full page.
When this is used the script should only contain a single Streamlit widget
in the main block container (i.e. using a st.sidebar will not affect the 
main container).

Returns
-------
None
"""
def set_last_component_full_page():
    set_appview_padding(0)
    set_main_container_height_width(height="100%", width="100%")
    set_vertical_block_gap(0)
    set_last_component_height_width(height="100%", width="100%")


"""
Injects the contents of a file into an html style tag using st.markdown.

Returns
-------
Return value of st.markdown
"""
def inject_local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


"""
Injects the contents of a file into an html script tag using st.html.

Returns
-------
Return value of st.html
"""
def inject_local_script(file_name):
    with open(file_name) as f:
        components.html(f'<script>{f.read()}</script>', height=0)