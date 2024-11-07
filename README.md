# Google Email Scraper and Sender

This Python project is designed to automate email outreach for agency owners. It combines web scraping using Google Search API and Selenium with email automation to find, verify, and send personalized emails to potential clients.

## Features

- **Google Search Scraping:** Scrapes Google search results for email addresses based on specified keywords, websites, and mail types.
- **Selenium-Based Scraping:** Uses Selenium for websites where Google Search API might not be effective.
- **Email Verification:** Verifies email addresses to reduce bounce rates.
- **Duplicate Removal:** Removes duplicate emails from the collected list.
- **Email Personalization:** Randomizes email templates and subject lines for a more personalized touch.
- **Email Sending:** Sends emails through Gmail accounts using SMTP.
- **Streamlit Web App:** Provides a user-friendly interface for managing the scraping and sending process.

## Files

- **app.py:** Main Streamlit application file for user interaction.
- **pages/Email_Sender.py:** Streamlit page for email sending functionality.
- **test.py:** Testing script (currently for UI elements).
- **cli-email-sender.py:** Command-line interface for email sending (incomplete).
- **functions.py:** Contains all the core functions for scraping, verification, and sending emails.

## Requirements

- Python 3.7+
- Libraries: `requests`, `re`, `smtplib`, `email`, `random`, `time`, `ssl`, `pandas`, `selenium`, `webdriver_manager`, `dns.resolver`, `json`, `streamlit`
- Gmail accounts for sending emails (credentials stored in `emails.json`)

## Installation

1. Clone the repository: `git clone https://github.com/MuhammadShahzeb123/Gmail-Finder-and-Sender.git`
2. Navigate to the project directory: `cd Gmail-Finder-and-Sender`
3. Install the required libraries: `pip install -r requirements.txt`
4. Configure Gmail credentials in `emails.json`.

## Usage

1. **Streamlit App:**
   - Run the app: `streamlit run app.py`
   - Use the web interface to specify search parameters, select websites, and initiate scraping and sending.
2. **Command-Line Interface (Incomplete):**
   - The `cli-email-sender.py` file is intended for command-line usage but is currently incomplete.

## Configuration

- **emails.json:**
  - Create the emails.json file using emails.json.example.
  - Store Gmail account credentials in this file.
  - Format:
    ```json
    [
      {
        "sender_email": "your-email@gmail.com",
        "sender_password": "your-password"
      },
      {
        "sender_email": "another-email@gmail.com",
        "sender_password": "another-password"
      }
    ]
    ```

## Disclaimer

- This project is for educational purposes only.
- Scraping websites and sending unsolicited emails may violate their terms of service. Use responsibly and ethically.
- Always obtain consent before sending marketing emails.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.
