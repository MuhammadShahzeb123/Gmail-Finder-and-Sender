import requests
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from time import sleep
import ssl
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


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
  match = re.search(email_regex, text)
  if match:
    return match.group(0)  # Return the matched string
  else:
    return None 

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
        "you’ll never cold email again…",
        "🎯 automate every client-getting task!",
        "you need this client-getting hack!",
        "you won’t chase clients anymore…",
        "🤖 new tool, no more outreach…",
        "what iF OutREach WAsn't Your proBlem anyMOre?",
        "you’ve been doing outreach wrong…",
        "🤯 this tool does all the outreach…",
        "🚀 stop client outreach forever!",
        "🎯 automate lead gen with AI…",
        "📧 AI sending your next client email?",
        "you won’t believe this lead machine…"
    ]
    
    # Randomly select a subject line from the list
    return random.choice(subject_lines)

def send_email(recipient_email: str, subject: str, message_text: str) -> bool:
    # Sender email and SMTP server details
    # sender_email = "zebzcops@gmail.com"
    # sender_password = "qvcm dcto yevw nxkn"  
    sender_email = "shahzebnaveed621@gmail.com"
    sender_password = "fmrf lvkg fdis yclt"  # Replace with your email password
    smtp_server = "smtp.gmail.com"
    smtp_port = 465  # Port number for SSL

    try:
        # Create the MIME message
        msg = MIMEMultipart()
        msg['From'] = f"Email AI -> <{sender_email}>"
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_text, 'plain'))

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to the SMTP server using SSL
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)  # Login with email and password
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send email

        return True  # Return True if email is successfully sent

    except Exception as e:
        print(f"Failed to send email: {e}")
        return False  # Return False if there's any issue

def update_email_list(new_email: str) -> None:
    # Load the existing emails into a DataFrame
    try:
        emails_df = pd.read_csv("./pages/emails.txt", header=None, names=["email"], encoding="utf-8")
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty DataFrame
        emails_df = pd.DataFrame(columns=["email"])

    # Append the new_email to the send_to_emails.txt file
    with open("./pages/send_to_emails.txt", "a", encoding="utf-8") as f:
        f.write(new_email + "\n")

    # Remove any whitespace or newlines and check if new_email exists
    emails_df['email'] = emails_df['email'].str.strip()
    if new_email in emails_df['email'].values:
        emails_df = emails_df[emails_df['email'] != new_email]

    # Write the updated email list back to the emails.txt file
    emails_df.to_csv("./pages/emails.txt", index=False, header=False, encoding="utf-8")
              
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
        filtered_emails = [email for email in unique_emails if email not in sent_emails]

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

    # Configure Selenium webdriver
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
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
