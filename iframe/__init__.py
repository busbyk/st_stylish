import os
import streamlit as st
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component("stylish_iframe", url="http://localhost:3001")
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("stylish_iframe", path=build_dir)


def stylish_iframe(
    src = None,
    srcdoc = None,
    width = None,
    height = None,
    scrolling = False,
):
    """Create a new instance of "stylish_iframe".

    Parameters
    ----------
    src : str
        The URL of the page to embed.
    srcdoc : str
        Inline HTML to embed. Overrides src.
    width : int
        The width of the frame in CSS pixels. Defaults to the app's
        default element width.
    height : int
        The height of the frame in CSS pixels. Defaults to 150.
    scrolling : bool
        If true, show a scrollbar when the content is larger than the iframe.
        Otherwise, never show a scrollbar.

    Returns
    -------
    null

    """
  
    return _component_func(src=src, srcdoc=srcdoc, width=width, height=height, scrolling=scrolling, default=None)
