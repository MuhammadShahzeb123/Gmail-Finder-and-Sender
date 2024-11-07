from functions import *
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env

API_KEY0 = os.environ.get('GOOGLE_API_KEY_SEARCH')
API_KEY1 = os.environ.get('GOOGLE_API_KEY_SEARCH_621')
API_KEY2 = os.environ.get('GOOGLE_API_KEY_SEARCH_622')



EMAIL = """
Hi

{If you’re in the service business then Guess what? you can ditch the outreach and ads to get clients now!|I've got some awesome news! If you’re running a service-based business, you don’t need to stress about outreach or ads to get clients anymore.|Big news! If you run a service business, you don’t have to deal with outreach or ads for clients anymore.|Quick heads-up: If you run a service-based biz, you can forget about outreach and ads for getting clients!|Skip the ads, skip the outreach. Here’s the smart way to land clients.|Tired of spending hours on client outreach with limited results? There’s a better way now with AI!|Imagine if getting new clients for your service-based business didn’t require constant outreach!|Ever thought there could be a simpler way to bring in clients without endless outreach?|Tired of the slow, manual hustle for new clients? An AI Automated approach might change everything.|Running a service business can feel like a grind when it comes to finding clients, right? But what if there’s a new way to speed that up?|It’s no secret that finding clients can be a slow process. What if you could make it easier with a fresh approach?|Reaching new clients can sometimes feel like a slow climb, can’t it? Here’s a thought—AI could lighten the load.|If growing your client list has been a challenge, you might want to hear about a new possibility.|You’ve likely noticed how time-consuming outreach can be for a service business. Here’s an approach that might shake things up.}

{I've developed a tool that will scrape the leads, write the Emails and send them automatically, Automatically!|Hey, I’ve created a tool that handles everything—finding leads, writing emails, and sending them out, all on autopilot.|You’re gonna love this—I built a tool that finds leads, writes emails, and sends them automatically. You don’t have to do a thing!|I’ve come up with a tool that’ll take care of everything—finding leads, writing emails, and sending them, all by itself!|Imagine a tool that does it all: finds the right leads, crafts the emails, and sends them out—completely automated.|I’ve built a tool that takes care of everything for you—from finding leads to writing and sending emails—all automatically.|With my new tool, the entire outreach process is handled for you—finding, writing, and sending emails, all in one.|I’ve designed a tool that takes over the outreach process, using AI to find leads, craft messages, and send them out automatically using AI.|Think about having a tool that finds the clients you need, writes the perfect emails, and sends them—all without you lifting a finger.|This tool does the heavy lifting: finds your leads, writes the emails, and sends them—completely on autopilot.|I’ve built a tool that turns outreach into a hands-off process, automatically finding leads, drafting messages, and sending them.|Picture a tool that takes over the entire client outreach process, finding leads and sending emails, fully automated.}

{As soon as someone replies, the AI steps in, replies back, nurtures the lead, and keeps things moving toward booking a call.|The AI tracks replies and automatically sends a response, handling lead nurturing for you—calls get booked without you doing a thing|If someone replies to your email, the AI tracks it, replies automatically, nurtures the lead, and helps you book calls seamlessly|Replies are handled by the AI—it automatically responds, nurtures the lead, and works to book calls, all while you focus on other things.|When someone replies, the AI steps in to handle everything—tracking responses, nurturing leads, and guiding them to book a call.|The AI checks for replies regularly, responds instantly, nurtures the lead, and helps move things toward an appointment, all on autopilot.|Once a lead responds, the AI takes over, replying, nurturing the conversation, and working toward booking a call for you.|Every reply is automatically managed by the AI, which responds, nurtures the lead, and guides them seamlessly toward an appointment.|The AI steps in with every reply, responding, nurturing, and setting up appointments, so you’re free to focus on other areas.|Any reply is captured by the AI, which takes care of follow-ups, lead nurturing, and guiding them toward a call—all hands-free.|Each lead reply is managed by AI, responding promptly, nurturing the relationship, and steering them to book a call without any manual work.}

{So, all that’s left for you to do is hop on a call, close the client, and watch the cash roll in. I’ve got everything else covered|All you’ve gotta do is take the call, seal the deal, and the money’s yours. I’m taking care of everything else|You handle the call and close the deal—that’s it! I’m taking care of everything else so you can just focus on making money.|All you have to worry about is closing the client on the call, then sit back and make money. I’ve already done all the hard work!|All that’s left for you is to jump on the call, close the deal, and start bringing in revenue. Everything else is handled.|Just focus on the calls and securing your clients—I’ve already set up the system to do the rest for you.|Your only task is to close the deal on the call. I’ve taken care of everything else so you can focus on growing your business.|With everything automated, all you need to do is show up, close the client, and see the profits come in.|I’ve set up the whole process—just focus on the call and turning leads into clients, while the tool manages everything else.|All you have to do is get on the call and secure the client. I’ve done the groundwork to ensure your pipeline is always full.|The tool handles every step, so you only need to take the calls and lock in your clients—simple and effective.|All you have to do is jump on the calls and close. I’ve created the process so you can focus entirely on delivering to your clients.|Everything is ready for you to just take the call and bring in the business. The rest is handled on autopilot.}

{Funny thing is, I didn’t even send you this email—the system I built did it for me! It found your business and sent this automatically.|Here’s the crazy part—I didn’t actually send you this email. My system did, all by itself, after finding your business in the niche I set!|Believe it or not, this email came from the system I built, not me! It found your business and sent this message on its own|The best part? I didn’t even send this email myself—my system found your business and reached out automatically!|Here’s the kicker—I didn’t send this email. The system I built did, after identifying your business as a match!|Believe it or not, this email came to you automatically through the tool I created. It found and reached out to your business on its ow|Crazy as it sounds, I didn’t send you this email—my AI system did! It found your business and sent this message without my input.|What’s amazing is that my system sent you this email by itself, after automatically finding your business in the ideal niche.|Hard to believe, but this email wasn’t even from me—my system found your business and handled the rest on its own.|Here’s the twist: my system sent this email, not me! It found your business and handled the outreach without me lifting a finger.|Here’s the real surprise—I’m not the one who sent this email! My system found your business and reached out all on its own.|Funny thing, I’m not the one who sent you this email—my automated system did. It identified your business and reached out independently!}

{If you reply to this email, just know the AI will respond and guide you to book a call—so save yourself the time and just book a call directly|FYI, if you reply to this email, the AI will respond and direct you to book a call. You can skip all that and just book it now!|Replying will get an AI response telling you to book a call, so save the time and hassle—just book it right from here|If you reply, you'll be chatting with an AI that will simply guide you to book a call—let's save time and book directly!|Any reply to this email will get an automated AI response nudging you to book a call, so let’s cut to the chase and book now.|The AI will answer any reply, redirecting you to book a call anyway, so go ahead and reserve your time now!|Just so you know, replying to this email connects you to an AI that will guide you to schedule a call—skip the extra steps and book now!|This email is automated, and any reply will only lead you to a call booking prompt. Why wait? Go ahead and book now.|If you hit “reply,” you’ll reach an AI that will suggest you book a call anyway—let’s make it easier and book directly!|Be aware that replies will connect you to an AI that will prompt you to book a call. Get ahead and secure your slot now!|Any response will be met with an AI suggesting you book a call—so let’s keep it simple and schedule a time right away.|I won't reply 'cause replying will connect you to an my AI that will guide you to book a call—save time and schedule directly!}

{Here you go: https://calendly.com/zcops/auto-ai-outreach |Book the Call Here: https://calendly.com/zcops/auto-ai-outreach |Simple Click here: https://calendly.com/zcops/auto-ai-outreach|Take the Lead—Book Your Call Now: https://calendly.com/zcops/auto-ai-outreach|Own It—Reserve Your Time: https://calendly.com/zcops/auto-ai-outreach|Claim Your Time Here: https://calendly.com/zcops/auto-ai-outreach|Take the Next Step—Book Here: https://calendly.com/zcops/auto-ai-outreach|Show Initiative—Schedule Now: https://calendly.com/zcops/auto-ai-outreach|Go for It—Lock in Your Call: https://calendly.com/zcops/auto-ai-outreach}

{Best. Looking forward to meeting with ya!|Can’t wait to connect with you soon!|Looking forward to an awesome convo!|Excited to meet—see you soon!|Looking forward to our chat—let’s make it great!|Ready to connect—see you soon!|Excited to chat—see you there!|Let’s make it a productive one—looking forward to it!}


Shahzeb Naveed
CEO
ZCopS

P.S: {I’m developing AI that will locate the exact business emails you need, gather lead-specific insights, and write personalized emails—all without my input.|Soon, my AI will automatically find the right business contacts, gather personal insights, and create targeted emails that stand out.|I'm adding features that will enable the AI to find professional emails, collect recent lead insights, and tailor messages that make a real impact.|Coming up: my AI will source business contacts, gather personalized info, and write each email with current insights on your leads.|Next up: an AI that autonomously finds business emails, pulls recent events, and crafts emails that resonate with each unique contact.|My upcoming AI tool will identify business emails, pull detailed lead data, and create one-of-a-kind, personalized outreach for you.|I’m building AI that locates professional contacts, gathers personal lead insights, and writes custom emails that make a lasting impression.|My new AI will soon be able to find professional contacts, scrape timely lead info, and generate hyper-personalized emails automatically.|The next upgrade will let my AI locate business emails, gather fresh insights on each lead, and craft emails tailored just for them.|Soon, my AI will not only locate business contacts but also collect recent lead info to craft customized, relevant emails that truly connect.}
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
