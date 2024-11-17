from functions import *
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env

API_KEY0 = os.environ.get('GOOGLE_API_KEY_SEARCH_ZEB')
API_KEY1 = os.environ.get('GOOGLE_API_KEY_SEARCH_HACK')
API_KEY2 = os.environ.get('GOOGLE_API_KEY_SEARCH_621')


SEARCH_ENGINE_ID = '826dfb73d8c7347d9'


st.title("Google Email Scraper")

site_options = ['instagram.com', 'facebook.com', 'x.com', 'reddit.com', 'quora.com', 'tumblr.com', 'tiktok.com', 'pinterest.com', 'dribbble.com', 'skool.com', 'Alignable.com' ]

selected_sites = {}

st.header("Select Websites")


# Calculate how many items to put in each column
num_columns = 4  # You can adjust this if needed
items_per_column = (len(site_options) + num_columns - 1) // num_columns

# Create columns
cols = st.columns(num_columns)

# Distribute checkboxes across columns
for st.session_state.number_of_emails_sent_today, site2 in enumerate(site_options):
    col_index = st.session_state.number_of_emails_sent_today // items_per_column  # Determine which column to use
    with cols[col_index]:
        selected_sites[site2] = st.checkbox(site2, value=True)

# Get a list of checked sites (same as before)
checked_sites = [site for site, checked in selected_sites.items() if checked]


col1, col3 = st.columns(2)
col4, col5 = st.columns(2)


with col1:
    st.header("Keyword")
    keyword = st.text_input("Enter keyword")


with col3:
    st.header("Mail Type")
    mailtype = st.text_input("Enter mail type", value="@gmail.com")
    
with col4:
    st.header("Start Number")
    start = st.number_input("Enter stop number", value=1)

with col5:
    st.header("Stop Number")
    stop = st.number_input("Enter stop number", value=100)
    

ocol1, ocol2 = st.columns(2)

with ocol1:
    options = ["shahzebnaveed625", "shahzebnaveed622", "hackerhandbookk", "shahzebjutt620", "shahzebnaveed623"]

    selected_option = st.selectbox("Select an option:", options)
    if selected_option == "shahzebnaveed625":
        email_selected = 0
    elif selected_option == "shahzebnaveed622":
        email_selected = 1
    elif selected_option == "hackerhandbookk":
        email_selected = 2
    elif selected_option == "shahzebjutt620":
        email_selected = 3
    elif selected_option == "shahzebnaveed623":
        email_selected = 4
    
    

with ocol2:
    api_options = ["API 0", "API 1", "API 2"]

    API_KEY = st.selectbox("Select an API Key", api_options)
    if API_KEY == "API 0":
        API_KEY = API_KEY0
    elif API_KEY == "API 1":
        API_KEY = API_KEY1
    elif API_KEY == "API 2":
        API_KEY = API_KEY2

break_point = int(st.number_input("Number of Emails to send:", value=1250))
st.session_state.number_of_emails_sent_today = 0 
additional_arguments = st.text_input("Addiotional Arguments for Google Search")

if st.button("Search and Send"):
    if checked_sites != []:
        for site in checked_sites:
            if keyword and mailtype and site:
                st.success("Searching " + site)
                search_results = google_search_api(keyword, site, mailtype, API_KEY, SEARCH_ENGINE_ID, start, stop)
                st.success("Google Search API Called!")
                google_search_api_emails = []
                st.write(len(search_results))
                for itm in search_results:
                    for item in itm.get('items', []):
                        extracted_emails = extract_email(item['snippet'])
                        
                        # Handle cases where `extract_email` returns a list
                        if isinstance(extracted_emails, list):
                            google_search_api_emails.extend(extracted_emails)  # Add all emails to main list
                        elif extracted_emails:  # In case it returns a single email
                            google_search_api_emails.append(extracted_emails)

                # Write emails to a file
                with open('./pages/emails_new.txt', "a+", encoding="utf-8") as f:
                    for itm in google_search_api_emails:
                        if itm is None:
                            continue
                        f.write(itm + "\n")  # Ensure itm is a string
                        
                with open('./pages/emails_new2.txt', "a+", encoding="utf-8") as f:
                    for itm in google_search_api_emails:
                        if itm is None:
                            continue
                        f.write(itm + "\n")  # Ensure itm is a string
                
            # Remove duplicates from emails.txt
    remove_duplicate_emails("./pages/emails_new.txt")

    # Send emails in a loop
    while True:
        with open('./pages/emails_new.txt', 'r', encoding='utf-8') as f:
            sent_to_email = f.readline()
            
        if sent_to_email != "":
            sleep(10)
            if verify_email(sent_to_email):
                sent_to_email = sent_to_email.strip()
                
                subject_line = get_random_subject_line()
                randomized_email = change_email_msg(EMAIL)
                
                # Send email
                email_sent, sender_email = send_email(sent_to_email, subject_line, randomized_email, email_selected)
                if email_sent:
                    st.success(f"Email wasn't sent to {sent_to_email} with {sender_email}")
                else:
                    st.write(f"Email wasn't sent to {sent_to_email} with {sender_email}")
                
                # Update email list and sleep
                update_email_list("./pages/emails_new.txt")           
                # Track the number of emails sent
                st.session_state.number_of_emails_sent_today += 1
                if st.session_state.number_of_emails_sent_today == break_point:
                    st.error("STOP! Limit Reached!")
                    break
            
                email_selected += 1
                if email_selected == 5:
                    email_selected = 0
            else:
                continue
        else:
            break

if st.button("Search and Send using Selenium"):
    for site in checked_sites:
        if keyword and site and mailtype:
            emails = google_search_selenium(keyword, site, mailtype, start, stop)
            
            with open('./pages/emails_new.txt', "a+", encoding="utf-8") as f:
                for itm in emails:
                    if itm is None:
                        continue
                    f.write(itm + "\n")
                f.close()
            
            remove_duplicate_emails("./pages/emails_new.txt")
            
            while True:
                with open('./pages/emails_new.txt', 'r', encoding= 'utf-8') as f: # Read an Email 
                    sent_to_email = f.readline()

                if sent_to_email != "":
                    if verify_email(sent_to_email) is False:
                        continue
                    sent_to_email = sent_to_email.strip()
                    subject_line = get_random_subject_line()
                    
                    randomized_email = change_email_msg(EMAIL)
                    email_sent, sender_email = send_email(sent_to_email, subject_line, randomized_email, email_selected)
                    if email_sent is True:
                        st.success(f"Email sent to {sent_to_email} with {sender_email}")
                        print(f"Email sent to {sent_to_email} with {sender_email}")
                    else:
                        st.write(f"Email wasn't sent to {sent_to_email} with {sender_email}")
                    update_email_list("./pages/emails_new.txt")
                    sleep(random.randint(5, 10))
                    st.session_state.number_of_emails_sent_today += 1
                    if st.session_state.number_of_emails_sent_today == 250:
                        if email_selected == 0:
                            email_selected = 1
                        elif email_selected == 1:
                            email_selected = 2
                        elif email_selected == 2:
                            email_selected = 0
                    
                    if st.session_state.number_of_emails_sent_today == break_point:
                        st.error("STOP! Limit Reached!")
                        break
                else:
                    break
        
if st.button("Remove Duplicates"):
    remove_duplicate_emails("./pages/emails_new.txt")
