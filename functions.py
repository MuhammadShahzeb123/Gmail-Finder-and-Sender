import requests
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from time import sleep
import ssl
import pandas as pd



def google_search(keyword:str, site:str, mailtype:str, api_key:str, cse_id:str, start: int ,stop: int) -> list:
    """
    Make an API call to the Google Custom Search API and return the results.
    
    You can add how many results you want in `result_no`
    
    `result_no` MUST be a factor of 10
    
    Each page has only 9-10 emails.
    """
    dics = []
    for i in range(start, stop, 10): 
    # ... rest of your code
        query = f'{keyword} site:{site} "{mailtype}"'
        url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'q': query,
            'key': api_key,
            'cx': cse_id,
            'start': i
        }
        response = requests.get(url, params=params)
        print(response.json())
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
        "What If You Never Had to Do Outreach Again?",
        "How Much Time Are You Wasting on Outreach?",
        "The Hidden Time Killer in Your Agency",
        "You’re Spending Too Much Time on This…",
        "Here’s Why You’re Not Closing More Deals",
        "What If Outreach Wasn't Your Problem Anymore?",
        "How Much Time Is Outreach Really Costing You?",
        "The Silent Killer of Your Agency’s Growth",
        "You’re Losing Hours on This Task Every Week…",
        "This Is Why Your Close Rate Isn't Higher"
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
        msg['From'] = f"You know... <{sender_email}>"
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