from functions import *
import streamlit as st
import os


SEARCH_ENGINE_ID = '826dfb73d8c7347d9'
API_KEY = os.environ.get('GOOGLE_API_KEY_SEARCH')


st.title("Google Email Scraper")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.header("Keyword")
    keyword = st.text_input("Enter keyword")

with col2:
    st.header("Website")
    site = st.text_input("Enter website")

with col3:
    st.header("Mail Type")
    mailtype = st.text_input("Enter mail type")
    
with col4:
    st.header("Start Number")
    start = st.number_input("Enter stop number", value=1)

with col5:
    st.header("Stop Number")
    stop = st.number_input("Enter stop number", value=100)
    
    


if st.button("Search"):
    if keyword and site and mailtype:
        search_results = google_search(keyword, site, mailtype, API_KEY, SEARCH_ENGINE_ID, start, stop)
        email = []
        for itm in search_results:

            for item in itm.get('items', []):
                email.append(extract_email(item['snippet']))


        with open('./pages/emails.txt', "a+", encoding="utf-8") as f:
            for itm in email:
                if itm is None:
                    continue
                f.write(itm + "\n")
            f.close()
        
        str_of_emails = """"""
        for itm in email:
            if itm is None:
                continue
            str_of_emails += itm + "\n"
            
        st.write(str_of_emails)

if st.button("Remove Duplicates"):
    remove_duplicate_emails("./pages/emails.txt")