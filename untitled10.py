import streamlit as st

username = st.text_input("Username")
password = st.text_input("Password", type='password')

if st.button("Submit"):
    st.success("Username: {}, Password: {}".format(username, password))

if st.button("Download"):
    st.write("Downloading file...")
    with open('./aaa.pdf', "rb") as file:
        st.download_button(label="下载",
                           data=file,
                           file_name='./aaa.pdf',
                           mime='application/octet-stream',
                           )