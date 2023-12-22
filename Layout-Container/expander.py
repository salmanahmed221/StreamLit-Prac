# https://docs.streamlit.io/library/api-reference/layout/st.expander

import streamlit as st

with st.expander("See explanation"):
    st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're guaranteed to be random.")
    st.image("https://static.streamlit.io/examples/dice.jpg")