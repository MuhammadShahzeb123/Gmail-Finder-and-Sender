# 📧 Google Email Scraper 🚀

## Description 📝

This Python project is an email scraping and automation tool designed specifically for agency owners. It leverages the power of the Google Custom Search JSON API to find potential client email addresses and then automates personalized email outreach. 

## Features ✨

* **Targeted Email Scraping:** Scrape Google search results for email addresses based on:
    * **Keywords:** Target specific industries or niches.
    * **Websites:** Focus on particular platforms (e.g., Instagram, LinkedIn).
    * **Mail Types:** Filter by email domains (e.g., @gmail.com, @domain.com).
* **Duplicate Removal:** Automatically removes duplicate email addresses from the scraped results, ensuring a clean list.
* **Email Filtering:**  Excludes emails that have already been sent to, preventing redundant outreach.
* **Personalized Email Campaigns:**
    * **Customizable Email Templates:**  Craft engaging email messages tailored to your target audience.
    * **Randomized Subject Lines:** Increase open rates with a variety of subject lines.
    * **Automated Sending:**  Send emails efficiently with built-in delays to avoid spam filters.
* **Streamlit Web App:**  An intuitive user interface built with Streamlit for easy interaction and data visualization.

## Files 📁

* **`main.py`:** The main Streamlit application file. Handles user input, triggers the scraping process, displays results, and manages email sending.
* **`functions.py`:** Contains the core functions for:
    * `google_search()`: Makes API calls to the Google Custom Search API to retrieve search results.
    * `extract_email()`: Extracts email addresses from text using regular expressions.
    * `change_email_msg()`: Randomizes email template content for personalization.
    * `get_random_subject_line()`: Selects a random subject line from a list.
    * `send_email()`: Sends emails using SMTP with SSL encryption.
    * `update_email_list()`: Manages the list of sent emails to avoid duplicates.
    * `remove_duplicate_emails()`: Removes duplicate emails from the scraped list.
* **`pages/email_sender.py`:**  (Appears to be a duplicate of `Email_Sender.py`, consider removing one)
* **`pages/Email_Sender.py`:**  Contains the Streamlit code for the email sending interface.
* **`test.py`:** A basic script for testing the `google_search()` function.

## Installation 🧰

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/google-email-scraper.git
   cd google-email-scraper
   ```
2. **Create and Activate a Virtual Environment (Recommended): (This keeps your project dependencies organized! ✨)**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate 
    ```
3. **Install Dependencies: (Like a shopping list for your code! 🛒)**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set Up Environment Variables: (Your secret ingredients! 🤫)**
    - Create a .env file in the project root directory.
    - Add your Google Custom Search API key:
        ```bash
        GOOGLE_API_KEY_SEARCH=your_actual_api_key
        ```

## Usage 🚀 (Time to unleash the power! 💪)

1. **Run the Streamlit App:**
    ```bash
    streamlit run main.py
    ```
2. **Input Search Parameters: (Tell it what you're looking for! 🎯)**
    - Enter your desired keywords, website, and mail type.
    - Specify the start and stop numbers for the Google Search results pagination.

3. **Click on Search**
    - Click the "Search" button to initiate the email scraping process.

4. **Review and Send Emails: (Craft your message and connect! 💌)**
    - The scraped email addresses will be displayed.
    - Click the "Send Emails" button to start the email campaign.


## Disclaimer ⚠️ (Let's keep it ethical! 🙏)

1. This tool is intended for ethical and legal use cases only.
2. Always respect website terms of service and privacy regulations when scraping data.
3. Be mindful of email sending limits to avoid being flagged as spam.

## Contributing 🤝 (Want to make it even better? 🙌)

Contributions are welcome! Feel free to open issues or pull requests.

Remember to replace placeholders like your-username and your_actual_api_key with your actual information