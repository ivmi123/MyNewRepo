import streamlit as st
st.title("Моето първо Streamlit приложение")
name = st.text_input("Как се казваш?")
if name:
   st.write(f"Здравей, {name}!")
age = st.number_input(
    "Enter your age",
    min_value=0,
    max_value=120,
    step=1
)
if age:
    st.write(f"Your age is: {age}")
