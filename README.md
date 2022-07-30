# st_stylish

A collection of custom components and helper functions for Streamlit that are focused on providing advanced styling functionality.

The primary functionality in this repo is in the `/st_stylish/helpers.py` module. This module provides functions that inject css via the `st.markdown` hack that target elements in a more reliable way than the typical generated ids approach. Readable class names that should change much less frequently, DOM structure, and tag attribute names are used to target elements.

## Setup

### Local

1. Create a virtual environment
2. Activate your virtual environment
3. `pip install -r requirements.txt`

## Helper functions

### Use cases

1. Full page component
   Note: Make sure to set `layout='wide'` with `st.set_page_config(layout='wide')`

### Examples

#### Full page component

1. Single page - full page iframe `/examples/singlepage.py`

   Run it: `streamlit run ./examples/singlepage.py`

2. Multi page - full page iframe `/examples/multipage/__init__.py`

   Run it: `streamlit run ./examples/multipage/home.py`

3. Full page component using convenience function `/examples/fullpage_component.py`

   Run it: `streamlit run ./examples/fullpage_component.py`

4. Using the StyleInjector context manager `/examples/with_StyleInjector.py`

   Run it: `streamlit run ./examples/with_StyleInjector.py`

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

## Using the StyleInjector

If you want to style multiple components (i.e. `.element-container`s) you can use the StyleInjector class as a context manager like so:

```
with StyleInjector() as injector:
  injector.set_appview_padding(0)
```

The StyleInjector will keep track of the `components.markdown` calls. When you call the StyleInjector's `set_n_component_height_width` the index of the streamlit component will be offset by the number of previously injected markdown components.

So to style the first streamlit component that you call in the script, call `set_n_component_height_width` with an `index` argument of 0.

See `/examples/with_StyleInjector.py` for example code.

## Enhancements

1. ~~StylesManager class~~ (Done)
   I want to create a StylesManager class that controls the injection of `<style>` tags via `st.markdown` and keeps an index of `.element-container`s so we can target specific `.element-container`s to style independently. Right now the `set_component_height_width` function just targets the last streamlit element. This works great for a full page iframe, for example, but you then cannot add any more components below that iframe.

## TODO

- [x] convenience function for a full page component
- [x] add docstrings to all helper functions
- [x] implement StylesManager concept
- [ ] deploy to PyPi
