# st_stylish

A collection of custom components and helper functions for Streamlit that are focused on providing advanced styling functionality.

The primary functionality in this repo is in the `/st_stylish/helpers.py` module. This module provides functions that inject css via the `st.markdown` hack that target elements in a more reliable way than the typical generated ids approach. Readable class names that should change much less frequently, DOM structure, and tag attribute names are used to target elements.

## Helper function use cases

1. Full page component

### Examples

#### Full page component

1. Single page - full page iframe `/examples/singlepage.py`
2. Multi page - full page iframe `/examples/multipage/__init__.py`

## Custom components

1. iframe
   The only added functionality here is the loading indicator while the iframe content loads.

   To run this custom component's frontend locally:

   ```
   cd st_stylish/iframe/frontend
   npm install
   npm start
   ```

   Then you can use it in a streamlit file. From project root:
   `streamlit run examples/stylish_iframe.py`

## Enhancements

1. StylesManager class
   I want to create a StylesManager class that controls the injection of `<style>` tags via `st.markdown` and keeps an index of `.element-container`s so we can target specific `.element-container`s to style independently. Right now the `set_component_height_width` function just targets the last streamlit element. This works great for a full page iframe, for example, but you then cannot add any more components below that iframe.

## TODO

- convenience function for a full page component
- add docstrings to all helper functions
- implement StylesManager concept
