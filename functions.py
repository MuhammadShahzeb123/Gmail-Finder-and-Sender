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


with open('emails.json', 'r') as f:
    emails_and_passoword = json.load(f)


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
        "I want to finish this outreach problem",
        "can I fix this outreach problem with AI?",
        "let’s finally solve our outreach problem, yeah?",
        "can we just fix this outreach hassle already?",
        "🤖 new tool, no more outreach…",
        "what iF OutREach WAsn't Your proBlem anyMOre?",
        "you’ve been doing outreach wrong…",
        "Trying to crack this outreach code—thoughts?",
        "is this the end of our outreach headache (thanks to AI)?",
        "outreach struggles? Maybe AI’s got it.",
        "📧 AI sending your next client email?",
        "i don't want to believe this lead machine…"
    ]
    
    # Randomly select a subject line from the list
    return random.choice(subject_lines)

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

def send_email(recipient_email: str, subject: str, message_text: str, which_email: int = 0) -> list:
    # Sender email and SMTP server details
        
    if 0 <= which_email < len(emails_and_passoword):
        sender_email = emails_and_passoword[which_email]['sender_email']
        sender_password = emails_and_passoword[which_email]['sender_password']
    
    smtp_server = "smtp.rambler.ru"
    smtp_port = 465  # Port number for SSL

    try:
        # Create the MIME message
        msg = MIMEMultipart()
        msg['From'] = f"Shahzeb AI <{sender_email}>"
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_text, 'plain'))

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
    
def verify_email(email):
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

