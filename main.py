import streamlit as st
import  langchain_helper


st.title("Responsibility In Central Government")

position = st.sidebar.selectbox("Select position",("Prime-Minister","Home-minister","Finance-Minister","Defence-Minister"))

if position:
    response = langchain_helper.generate_response(position)
    st.write(response)
