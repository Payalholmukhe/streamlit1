import streamlit as st
from client import StockApi
 
# create page title
st.set_page_config("Stock Market App")
 
# add title
 
st.title("Stock Market App")
 
# add subheading
st.subheader("By Payal Holmukhe")
 
##
company = st.time_input("Company Name")
 
## create function for making connection between stockapp class and app
@st.cache_resource(ttl=3600)
def fetch_data():
    return StockApp()
 