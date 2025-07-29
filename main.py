import streamlit as st
import streamlit_option_menu
with st.sidebar :
  tab = option_menu (
    "Sci-Day",
    ['Home','About Sci-Day','Activities'],
    icon = ['home','book','game']
  )
