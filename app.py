from functions import *
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env

API_KEY0 = os.environ.get('GOOGLE_API_KEY_SEARCH_ZEB')
API_KEY1 = os.environ.get('GOOGLE_API_KEY_SEARCH_HACK')
API_KEY2 = os.environ.get('GOOGLE_API_KEY_SEARCH_621')


EMAIL = """
{Hi|Hey|Hello} 

{Running a business is tough enough without outreach headaches, right?|Outreach doesn’t have to feel like a never-ending grind.|Imagine spending less time chasing clients and more time serving them.|Struggling with outreach isn’t a bizz requirement—it’s an obstacle we can clear.|Have some time to read me about making outreach work for you, not against you.|What if getting clients felt effortless and natural instead of draining?|Client acquisition shouldn’t eat up all your energy—it can be easier.|Growth happens when outreach becomes efficient, not overwhelming, don't ya think?|It’s time to make client acquisition feel like a breeze, not a chore.}

{With my AI automation, you can skip the manual work and let tech handle the sending for you.|Imagine emails going out seamlessly while you focus on growing your business.|My Email AI can now handle the heavy lifting of outreach, so you don’t have to|Say goodbye to tedious email sending—My Email AI’s got that part covered.|My Email AI ensures your outreach emails are sent effortlessly, right on schedule.|No more juggling—My Email AI handles the outreach flow from leads to inboxes.|My AI-powered tools take the hassle out of sending emails, keeping outreach effortless.}

{Oh, I didn't mention but... It even finds the right people for you—no need to buy another email list, ever.|And yeah, it kinda stalks the Internet (in a good way) to grab the emails of the clients you actually want.|Oh, and guess what? It even hunts down emails of your dream clients online—so no more worrying about cold email lists.|Oh, and it’s got you covered on emails too—it scrapes the web for your perfect leads.}

{Beyond that, it even replies to emails and schedules appointments for you—all on autopilot.|+, it takes care of follow-ups and appointment scheduling, all without lifting a finger.|On top'a that, it responds to replies and manages bookings while you focus elsewhere.|It also handles client replies and secures meetings, leaving you free to focus on growth.}

{Finally, a way to make life easy—autopilot the busy stuff and focus on locking in clients.|So, all you’ve gotta do is show up for those booked calls and close, while AI does the rest.|You can now leave those tough parts for AI and just focus on turning those booked calls into wins.|It’s like having a cheat code—let AI line it all up, and you handle the fun part: closing deals.|You’re all set to make things easy—just sit back, handle the calls, and watch the cash roll in.}

{Funny thing is, this AI actually picked you as a perfect lead for me—so imagine what it can do for your business.|And yeah, the AI scraped your profile as a great match for this—just think how it’ll pinpoint your dream clients too.|To be real with you, if the AI found you as a perfect lead for me, imagine how spot-on it’ll be for your business.|Just so you know, the AI flagged you as a great fit—which means it can do the same for your target clients too.|To keep it straight, the AI singled you out as a perfect lead—now think about how it’ll work for you.|And yes, the AI spotted you as an ideal match for me—that’s exactly how it’ll help you nail your leads too.}

{So yeah, just hit me up if you wanna see how it works—I’m here to help.|Let me know if this sounds cool to you, and I’ll hook you up with the details.|Anyway, lemme know if you wanna try it out—no pressure, just thought it’d help.|Got any questions? Just shoot me a reply—I’m chill and happy to explain more.|Think it’s worth a shot? Just let me know, and I’ll get you set up in no time.}


Shahzeb Naveed
AI Automation Expert | Python Developer
CEO at ZCopS
"""



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
