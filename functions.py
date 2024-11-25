import requests
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from time import sleep
import ssl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import dns.resolver
import json


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


with open('emails.json', 'r') as f:
    emails_and_password = json.load(f)


PROXIES = [
    ("198.23.239.134", "6540", "msimyhie", "iuo7t7wzak7j"),
    ("207.244.217.165", "6712", "msimyhie", "iuo7t7wzak7j"),
    ("107.172.163.27", "6543", "msimyhie", "iuo7t7wzak7j"),
    ("64.137.42.112", "5157", "msimyhie", "iuo7t7wzak7j"),
    ("173.211.0.148", "6641", "msimyhie", "iuo7t7wzak7j"),
    ("161.123.152.115", "6360", "msimyhie", "iuo7t7wzak7j"),
    ("167.160.180.203", "6754", "msimyhie", "iuo7t7wzak7j"),
    ("154.36.110.199", "6853", "msimyhie", "iuo7t7wzak7j"),
    ("173.0.9.70", "5653", "msimyhie", "iuo7t7wzak7j"),
    ("173.0.9.209", "5792", "msimyhie", "iuo7t7wzak7j")
]

def get_random_proxy():
    # Select a random proxy
    ip, port, user, password = random.choice(PROXIES)
    proxy_url = f"http://{user}:{password}@{ip}:{port}"
    
    # Set up proxy dictionary
    proxy_dict = {
        "http": proxy_url,
        "https": proxy_url
    }
    return proxy_dict

def fetch_with_random_proxy(url): #Use this to Verify Emails
    # Get a random proxy
    proxy = get_random_proxy()
    
    try:
        # Make the request with the proxy
        response = requests.get(url, proxies=proxy, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Request failed with proxy {proxy}: {e}")
        return None

def google_search_api(keyword:str, site:str, mailtype:str, api_key:str, cse_id:str, start: int ,stop: int) -> list:
    """
    Make an API call to the Google Custom Search API and return the results.
    
    You can add how many results you want in `result_no`
    
    `result_no` MUST be a factor of 10
    
    Each page has only 9-10 emails.
    """
    dics = []
    for i in range(start, stop, 10): 
        query = f'{keyword} site:{site} "{mailtype}"'
        url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'q': query,
            'key': api_key,
            'cx': cse_id,
            'start': i
        }
        response = requests.get(url, params=params)
        dics.append(response.json())
        print(i)
    
    return dics

def extract_email(text):
    """
    Extracts all email addresses from the given text using a regular expression.

    Args:
      text: The text to search within.

    Returns:
      A list of extracted email addresses, or an empty list if none are found.
    """
    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    matches = re.findall(email_regex, text)  # Find all email matches
    cleaned_emails = [email.strip('"-') for email in matches]  # Remove unwanted characters like '-' or '"'
    return cleaned_emails if cleaned_emails else None

def change_email_msg(template: str) -> str:
    # Regular expression to match {...} blocks
    pattern = r"\{(.*?)\}"
    
    # Function to randomly select one of the options within each {...}
    def select_random(match):
        options = match.group(1).split('|')  # Split the content by |
        return random.choice(options)  # Randomly choose one
    
    # Substitute all {...} blocks with the randomly selected option
    result = re.sub(pattern, select_random, template)
    
    return result

def get_random_subject_line() -> str:
    # List of subject lines
    subject_lines = [
        "AI?",
        "can we just fix this outreach hassle already??",
        "what iF OutREach WAsn't Your proBlem anyMOre?!",
        "can I fix this outreach problem with AI?!",
        "you’ve been doing outreach wrong…",
        "tryna crack this outreach code—thoughts...",
        "is this the end of our outreach headache (thanks to AI)?",
        "outreach struggles? Maybe AI’s got it.",
        "i don't want to believe this lead machine…"
    ]
    
    # Select 4 unique random subject lines
    final_subject_lines = random.sample(subject_lines, 4)
    
    # Return one of the selected subject lines
    return random.choice(final_subject_lines)

def update_email_list(file_path: str) -> None:
    try:
        with open(file_path, "r") as f:
            emails = f.readlines()
        
        with open("./pages/send_to_emails.txt", "a+", encoding="utf-8") as f:
            f.write(emails[0])
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(emails[1:])    
    except:
        pass
              
def remove_duplicate_emails(file_path: str) -> None:
    """
    Removes duplicate emails from the given file and filters out emails 
    that are already present in "send_to_emails.txt".

    Args:
        file_path (str): The path to the file containing the emails.
    """
    try:
        # Step 1: Read all emails from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            emails = file.readlines()

        # Step 2: Remove duplicates by converting the list to a set and then back to a list
        unique_emails = list(set(email.strip() for email in emails))

        # Step 3: Read emails from "send_to_emails.txt"
        try:
            with open("./pages/send_to_emails.txt", 'r', encoding='utf-8') as sent_file:
                sent_emails = set(email.strip() for email in sent_file.readlines())
        except FileNotFoundError:
            sent_emails = set()  # If the file doesn't exist, assume no emails have been sent

        # Step 4: Filter out emails that are already in "send_to_emails.txt"
        filtered_emails = [
            email for email in unique_emails 
            if email not in sent_emails and len(email.split('@')[0]) >= 7 and email.startswith("-") == False
        ]
        # Step 5: Sort the emails (optional)
        filtered_emails.sort()

        # Step 6: Write the filtered emails back to the original file
        with open(file_path, 'w', encoding='utf-8') as file:
            for email in filtered_emails:
                file.write(email + '\n')

        print(f"Duplicate emails removed and filtered successfully from {file_path}.")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def extract_email(text: str) -> list:
    """
    Extracts all email addresses from the given text using a regular expression.

    Args:
        text: The text to search within.

    Returns:
        A list of extracted email addresses, or an empty list if none are found.
    """
    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Z|a-z]{2,7}"
    matches = re.findall(email_regex, text)
    return matches

def google_search_selenium(keyword: str, site: str = "instagram.com", mailtype: str = "@gmail.com", start: int = 0, stop: int = 201):
    """
    Searches Google using Selenium, extracts all text from each search result page,
    and then extracts email addresses matching the given criteria.

    Args:
        keyword (str): The keyword to search for.
        site (str): The website to restrict the search to.
        mailtype (str): The email domain to search for (e.g., '@gmail.com').
        start (int): The starting page number (default: 0).
        stop (int): The ending page number (exclusive, default: 201 for 20 pages).

    Returns:
        list: A list of extracted email addresses.
    """
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    extracted_emails = []

    # Construct the search query
    query = f'{keyword} site:{site} "{mailtype}"'

    for i in range(start, stop, 10):
        try:
            driver.get(f"https://www.google.com/search?q={query}&start={i}")

            # Wait for the page to load (adjust timeout as needed)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )

            # Get all text from the page body
            page_text = driver.find_element(By.TAG_NAME, 'body').text

            if "Make sure that all words are spelled correctly." in page_text and "Try different keywords." in page_text:
                break
            # Extract emails from the entire page text
            emails = extract_email(page_text)
            if emails:
                extracted_emails.extend(emails)

            # Add a delay between page loads (optional but recommended)
            sleep(20)  # Wait for 20 seconds before going to the next page
        except Exception as e:  # Catch WebDriver exceptions
            print(f"WebDriver error occurred: {e}")
            if "chrome not reachable" in str(e).lower():  # Check for window closed error
                print("Driver window closed manually. Returning collected emails.")
                return extracted_emails  # Return collected emails
            else:
                break  # Break for other WebDriver errors
    # Close the browser
    driver.quit()

    return extracted_emails

def send_email(recipient_email: str, subject: str, message_text: str, which_email: int = 1) -> list:
    # Sender email and SMTP server details
        
    if 0 <= which_email < len(emails_and_password):
        sender_email = emails_and_password[which_email]['sender_email']
        sender_password = emails_and_password[which_email]['sender_password']
    # sender_email = "me2@shahzeb.online"
    # sender_password = "ZCopS.com@12345678"

    smtp_server = "smtp.zoho.com"
    smtp_port = 465  # Port number for SSL

    try:
        # Create the MIME message
        msg = MIMEMultipart()
        msg['From'] = f"Shahzeb <{sender_email}>"
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_text, 'html'))

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to the SMTP server using SSL
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)  # Login with email and password
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send email

        return [True,sender_email] # Return True if email is successfully sent

    except Exception as e:
        print(f"Failed to send email: {e}")
        return [False, sender_email]  # Return False if there's any issue
    
def verify_email(email) -> bool:
    domain = email.split('@')[1]
    try:
        # Get MX records for the domain
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(mx_records[0].exchange)
        
        # Connect to the SMTP server
        server = smtplib.SMTP(mx_record)
        server.set_debuglevel(0)
        server.helo()
        server.mail(random.choice(["zaryabhaider888@gmail.com", "shahzebnaveed621@gmail.com", "shahzebnaveed622@gmail.com", "shahzebnaveed623@gmail.com", "shahzebnaveed624@gmail.com", "shahzebnaveed625@gmail.com", "zaryabhaider8888@gmail.com"]))  # Change to a valid email you control
        code, _ = server.rcpt(email)
        server.quit()
        return code == 250  # 250 means the email exists
    except dns.resolver.NoAnswer:
        print(f"No answer for the domain: {domain}")
        return False
    except dns.resolver.NXDOMAIN:
        print(f"The DNS query name does not exist: {domain}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def change_email_msg_html(template: str) -> str:
    # Regular expression to match {...} blocks
    pattern = r"\{(.*?)\}"
    
    # Function to randomly select one of the options within each {...}
    def select_random(match):
        options = match.group(1).split('|')  # Split the content by |
        return random.choice(options)  # Randomly choose one
    
    # Substitute all {...} blocks with the randomly selected option
    result = re.sub(pattern, select_random, template)
    
    subject_line = get_random_subject_line()
    
    # Create plain text version
    plain_text_version = result.replace("<br>", "\n").replace("<p>", "").replace("</p>", "")  # Convert HTML to plain text
    
    # HTML template with inline CSS
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject_line}</title>
    <style>
        body {{
            background-color: #f0f0f0; /* Light gray background */
            padding: 20px;
        }}
        .email-content {{
            background-color: #ffffff; /* White background for email body */
            color: #110010; /* Text color */
            font-size: 150%; /* Increase font size by 150% */
            font-family: Helvetica, Arial, sans-serif; /* Add more font options as needed */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(255, 255, 255, 0.5); /* Subtle shadow for depth */
        }}
        .hidden-preview {{
            display: none; /* Hide this when the email is opened */
            color: #100010; /* Ensure it's readable in preview */
        }}
    </style>
</head>
<body>
    <div class="hidden-preview">AI that has changed my Life and how I want it to ...</div>
    <div class="email-content">
        {result.replace("\n", "<br>")} <!-- Replace newlines with HTML line breaks -->
    </div>
</body>
</html>
    """
    
    # Combine both plain text and HTML into a multipart email format
    multipart_email = f"""MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="boundary_string"

--boundary_string
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 7bit

{plain_text_version}

--boundary_string
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

{html_template}

--boundary_string--
"""

    return multipart_email