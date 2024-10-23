from functions import *
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env

API_KEY = os.environ.get('GOOGLE_API_KEY_SEARCH')



EMAIL = """
Hi

{If you’re in the service business then Guess what? you can ditch the outreach and ads to get clients now!|I've got some awesome news! If you’re running a service-based business, you don’t need to stress about outreach or ads to get clients anymore.|Big news! If you run a service business, you don’t have to deal with outreach or ads for clients anymore.|Quick heads-up: If you run a service-based biz, you can forget about outreach and ads for getting clients!}

{I've developed a tool that will scrape the leads, write the Emails and send them automatically, Automatically!|Hey, I’ve created a tool that handles everything—finding leads, writing emails, and sending them out, all on autopilot.|You’re gonna love this—I built a tool that finds leads, writes emails, and sends them automatically. You don’t have to do a thing!|I’ve come up with a tool that’ll take care of everything—finding leads, writing emails, and sending them, all by itself!}

{As soon as someone replies, the AI steps in, replies back, nurtures the lead, and keeps things moving toward booking a call.|The AI tracks replies and automatically sends a response, handling lead nurturing for you—calls get booked without you doing a thing|If someone replies to your email, the AI tracks it, replies automatically, nurtures the lead, and helps you book calls seamlessly|Replies are handled by the AI—it automatically responds, nurtures the lead, and works to book calls, all while you focus on other things.}

{So, all that’s left for you to do is hop on a call, close the client, and watch the cash roll in. I’ve got everything else covered|All you’ve gotta do is take the call, seal the deal, and the money’s yours. I’m taking care of everything else|You handle the call and close the deal—that’s it! I’m taking care of everything else so you can just focus on making money.|All you have to worry about is closing the client on the call, then sit back and make money. I’ve already done all the hard work!}

{Funny thing is, I didn’t even send you this email—the system I built did it for me! It found your business and sent this automatically.|Here’s the crazy part—I didn’t actually send you this email. My system did, all by itself, after finding your business in the niche I set!|Believe it or not, this email came from the system I built, not me! It found your business and sent this message on its own}

{If you reply to this email, just know the AI will respond and guide you to book a call—so save yourself the time and just book a call directly|FYI, if you reply to this email, the AI will respond and direct you to book a call. You can skip all that and just book it now!|Replying will get an AI response telling you to book a call, so save the time and hassle—just book it right from here}

{Here you go: https://calendly.com/zcops/auto-ai-outreach |Book the Call Here: https://calendly.com/zcops/auto-ai-outreach |Simple Click here: https://calendly.com/zcops/auto-ai-outreach}

Best. Looking forward to meeting with ya!


Shahzeb Naveed

P.S: {I’m working on adding AI that’ll pull info from every lead and create super-targeted emails that’ll make them reach out to me for help.|Soon, my tool will grab lead info and use it to write personalized emails that make your ideal clients feel like I know exactly what they need|I'm adding a feature that’ll scrape every bit of data from leads, letting AI write emails that speak to their specific needs, making it easier for them to ask me for help.}
"""



SEARCH_ENGINE_ID = '826dfb73d8c7347d9'
print(API_KEY)


st.title("Google Email Scraper")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.header("Keyword")
    keyword = st.text_input("Enter keyword")

with col2:
    st.header("Website")
    site = st.text_input("Enter website", value="instagram.com")

with col3:
    st.header("Mail Type")
    mailtype = st.text_input("Enter mail type", value="@gmail.com")
    
with col4:
    st.header("Start Number")
    start = st.number_input("Enter stop number", value=1)

with col5:
    st.header("Stop Number")
    stop = st.number_input("Enter stop number", value=100)
    
    


if st.button("Search and Send"):
    if keyword and site and mailtype:
        search_results = google_search_api(keyword, site, mailtype, API_KEY, SEARCH_ENGINE_ID, start, stop)
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
        
        
        remove_duplicate_emails("./pages/emails.txt")
        
        with open('./pages/emails.txt', 'r', encoding= 'utf-8') as f:
            emails = f.readlines()
            
        while emails:
            sent_to_email = emails.pop()

            subject_line = get_random_subject_line()
            
            randomized_email = change_email_msg(EMAIL)
            email_sent: bool = send_email(sent_to_email, subject_line, randomized_email)
            if email_sent is True:
                st.success(f"Email sent to {sent_to_email}")
                print(f"Email sent to {sent_to_email}")
            else:
                st.write(f"Email wasn't sent to {sent_to_email}")
            update_email_list(sent_to_email)
            sleep(10)



if st.button("Search and Send using Selenium"):
    if keyword and site and mailtype:
        emails = google_search_selenium(keyword, site, mailtype, start, stop)
        
        with open('./pages/emails.txt', "a+", encoding="utf-8") as f:
            for itm in emails:
                if itm is None:
                    continue
                f.write(itm + "\n")
            f.close()
        
        remove_duplicate_emails("./pages/emails.txt")
        
        with open('./pages/emails.txt', 'r', encoding= 'utf-8') as f:
            emails = f.readlines()
                
        while emails:
            sent_to_email = emails.pop()
            subject_line = get_random_subject_line()
            
            randomized_email = change_email_msg(EMAIL)
            email_sent: bool = send_email(sent_to_email, subject_line, randomized_email)
            if email_sent is True:
                st.success(f"Email sent to {sent_to_email}")
                print(f"Email sent to {sent_to_email}")
            else:
                st.write(f"Email wasn't sent to {sent_to_email}")
            update_email_list(sent_to_email)
            sleep(10)



if st.button("Remove Duplicates"):
    remove_duplicate_emails("./pages/emails.txt")


st.header("Email Automation Tool")

st.write("This email sender tool is designed to automate outreach for agency owners. It scrapes Google search results for email addresses based on keywords, websites, and mail types you specify. The tool then removes duplicate emails and allows you to send personalized, randomized emails to the collected addresses. It includes features like customizable email templates, random subject line generation, and automatic updating of sent and remaining email lists. ")
