import streamlit as st
import Project

st.title("Restaurent name generator")

cuisine= st.sidebar.selectbox("Pick one",("Indian","Italian","Mexican"))

if cuisine:
    response = Project.generated(cuisine)
    st.header(response.content)
