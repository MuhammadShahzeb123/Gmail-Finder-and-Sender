from functions import *
import streamlit as st


EMAIL = """
Hi there,

{Are you spending too much time trying to reach potential clients, only to see minimal results?|Do you find yourself buried in the repetitive grind of prospecting, but not seeing the ROI you'd expect?|Is outreach taking up more time than it should, preventing you from scaling your agency?|Do you feel like managing outreach is eating into valuable time that could be spent growing your business?}

{Running an agency means juggling countless tasks, and client outreach shouldn't be one that drains your time.|As an agency owner, managing outreach across platforms is crucial but time-consuming.|Handling outreach manually, across multiple platforms, can be overwhelming and prone to errors.|Constantly switching between platforms for emails, DMs, and follow-ups can be exhausting and inefficient.}

{I offer a solution that streamlines your entire outreach process – a Done-For-You tool backed by AI that takes care of everything.|What if you could handle outreach, follow-ups, and even appointment bookings without lifting a finger?|Imagine having a tool that manages your outreach from emails to direct messages, and even schedules client appointments – all powered by AI.|Our software automates outreach across platforms, minimizing errors and boosting your agency's efficiency.}

{This software eliminates repetitive tasks and significantly reduces the chances of mistakes, thanks to its AI-driven system.|With an AI-powered tool managing your outreach, you'll see 99% accuracy and increased efficiency.|By automating your outreach with AI, you can focus on scaling your agency, while the tool takes care of all the details.|This AI-backed tool is designed to help you scale without getting bogged down in the time-consuming outreach process.|Our solution ensures that your outreach is handled with precision, so you can focus on growing your agency.}

{Let’s connect to discuss how this tool can be a game-changer for your agency.|Are you ready to automate your outreach and reclaim your time?|Can we schedule a quick call to explore how this can benefit your agency?|Would you like to see how this tool can free up your time and increase your client reach?|Let’s book a time to discuss how this can fit into your agency’s operations.}

Best. Looking forward to meeting with ya!


Shahzeb Naveed
"""

st.header("Email Automation Tool")

st.write("This email sender tool is designed to automate outreach for agency owners. It scrapes Google search results for email addresses based on keywords, websites, and mail types you specify. The tool then removes duplicate emails and allows you to send personalized, randomized emails to the collected addresses. It includes features like customizable email templates, random subject line generation, and automatic updating of sent and remaining email lists. ")


with open('./pages/emails.txt', 'r', encoding= 'utf-8') as f:
    emails = f.readlines()

if st.button("Send Emails"):
    while emails:
        
        with open('./pages/emails.txt', 'r', encoding= 'utf-8') as f: # Read an Email 
            sent_to_email = f.readline().strip()
            f.close()

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