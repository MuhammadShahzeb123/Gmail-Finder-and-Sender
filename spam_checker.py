# import requests
# import os
# import random
# import re


# API_KEY = os.environ.get('HUGGING_FACE_API')
# API_URL = "https://api-inference.huggingface.co/models/mshenoda/roberta-spam"
# headers = {"Authorization": f"Bearer {API_KEY}"}
# EMAIL = """
# {Hi|Hey|Hello} 

# {Running a business is tough enough without outreach headaches, right?|Outreach doesn’t have to feel like a never-ending grind.|Imagine spending less time chasing clients and more time serving them.|Struggling with outreach isn’t a bizz requirement—it’s an obstacle we can clear.|Have some time to read me about making outreach work for you, not against you.|What if getting clients felt effortless and natural instead of draining?|Client acquisition shouldn’t eat up all your energy—it can be easier.|Growth happens when outreach becomes efficient, not overwhelming, don't ya think?|It’s time to make client acquisition feel like a breeze, not a chore.}

# {With my AI automation, you can skip the manual work and let tech handle the sending for you.|Imagine emails going out seamlessly while you focus on growing your business.|My Email AI can now handle the heavy lifting of outreach, so you don’t have to|Say goodbye to tedious email sending—My Email AI’s got that part covered.|My Email AI ensures your outreach emails are sent effortlessly, right on schedule.|No more juggling—My Email AI handles the outreach flow from leads to inboxes.|My AI-powered tools take the hassle out of sending emails, keeping outreach effortless.}

# {Oh, I didn't mention but... It even finds the right people for you—no need to buy another email list, ever.|And yeah, it kinda stalks the Internet (in a good way) to grab the emails of the clients you actually want.|Oh, and guess what? It even hunts down emails of your dream clients online—so no more worrying about cold email lists.|Oh, and it’s got you covered on emails too—it scrapes the web for your perfect leads.}

# {Beyond that, it even replies to emails and schedules appointments for you—all on autopilot.|+, it takes care of follow-ups and appointment scheduling, all without lifting a finger.|On top'a that, it responds to replies and manages bookings while you focus elsewhere.|It also handles client replies and secures meetings, leaving you free to focus on growth.}

# {Finally, a way to make life easy—autopilot the busy stuff and focus on locking in clients.|So, all you’ve gotta do is show up for those booked calls and close, while AI does the rest.|You can now leave those tough parts for AI and just focus on turning those booked calls into wins.|It’s like having a cheat code—let AI line it all up, and you handle the fun part: closing deals.|You’re all set to make things easy—just sit back, handle the calls, and watch the cash roll in.}

# {Funny thing is, this AI actually picked you as a perfect lead for me—so imagine what it can do for your business.|And yeah, the AI scraped your profile as a great match for this—just think how it’ll pinpoint your dream clients too.|To be real with you, if the AI found you as a perfect lead for me, imagine how spot-on it’ll be for your business.|Just so you know, the AI flagged you as a great fit—which means it can do the same for your target clients too.|To keep it straight, the AI singled you out as a perfect lead—now think about how it’ll work for you.|And yes, the AI spotted you as an ideal match for me—that’s exactly how it’ll help you nail your leads too.}

# {So yeah, just hit me up if you wanna see how it works—I’m here to help.|Let me know if this sounds cool to you, and I’ll hook you up with the details.|Anyway, lemme know if you wanna try it out—no pressure, just thought it’d help.|Got any questions? Just shoot me a reply—I’m chill and happy to explain more.|Think it’s worth a shot? Just let me know, and I’ll get you set up in no time.}

# Shahzeb Naveed
# AI Automation Expert | Python Developer
# CEO at ZCopS
# """



# # Function to check spam/ham
# def check_spam(input_query):
#     payload = {"inputs": input_query}
#     response = requests.post(API_URL, headers=headers, json=payload)
#     response_data = response.json()
    
#     label_map = {
#         "LABEL_0": "Ham",
#         "LABEL_1": "Spam"
#     }
    
#     try:
#         results = []
#         for item in response_data[0]:
#             label = label_map.get(item['label'], "Unknown")
#             score = item['score']
#             results.append(f"{label}: {score:.6f}")
#         return results
#     except (KeyError, IndexError, TypeError) as e:
#         return f"Error parsing response: {e}\nResponse data: {response_data}"

# def change_email_msg(template: str) -> str:
#     # Regular expression to match {...} blocks
#     pattern = r"\{(.*?)\}"
    
#     # Function to randomly select one of the options within each {...}
#     def select_random(match):
#         options = match.group(1).split('|')  # Split the content by |
#         return random.choice(options)  # Randomly choose one
    
#     # Substitute all {...} blocks with the randomly selected option
#     result = re.sub(pattern, select_random, template)
    
#     return result


# # Main loop to take user input
# while True:
#     result = check_spam(EMAIL)
#     for line in result:
#         print(line)


import requests
import os
import itertools
import re
import json
from time import sleep

# Constants for the API
API_KEY = os.environ.get('HUGGING_FACE_API')
API_URL = "https://api-inference.huggingface.co/models/mshenoda/roberta-spam"
headers = {"Authorization": f"Bearer {API_KEY}"}

# Original email template
EMAIL_TEMPLATE = """
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

# Function to extract all options from the template
def extract_options(template):
    pattern = r"\{(.*?)\}"
    matches = re.findall(pattern, template)
    options = [match.split('|') for match in matches]
    return options

# Function to generate all possible combinations of the template
def generate_combinations(template):
    options = extract_options(template)
    combinations = list(itertools.product(*options))
    
    base_pattern = r"\{.*?\}"
    template_segments = re.split(base_pattern, template)
    
    for combination in combinations:
        email = ''.join([segment + choice for segment, choice in zip(template_segments, combination)])
        email += template_segments[-1]  # Append any trailing text after the last option
        yield email

# Function to check spam/ham using Hugging Face API
def check_spam(input_query):
    payload = {"inputs": input_query}
    response = requests.post(API_URL, headers=headers, json=payload)
    response_data = response.json()

    label_map = {
        "LABEL_0": "Ham",
        "LABEL_1": "Spam"
    }

    try:
        results = {}
        for item in response_data[0]:
            label = label_map.get(item['label'], "Unknown")
            score = item['score']
            results[label] = score
        return results
    except (KeyError, IndexError, TypeError) as e:
        return {"error": f"Error parsing response: {e}", "response_data": response_data}

# Main script to generate emails, check them, and save results incrementally
with open('spam_results.json', 'w') as file:
    file.write('[\n')  # Start the JSON array

    first_entry = True
    for email in generate_combinations(EMAIL_TEMPLATE):
        result = check_spam(email)
        if "error" in result:
            print(f"Error for email: {email[:50]}... - {result['error']}")
            continue

        spam_value = result.get("Spam", 0)
        ham_value = result.get("Ham", 0)
        email_entry = {
            "email": email,
            "spam_value": spam_value,
            "ham_value": ham_value
        }

        # Append to the file incrementally
        if not first_entry:
            file.write(',\n')  # Add a comma before subsequent entries
        json.dump(email_entry, file, indent=4)
        first_entry = False

        sleep(1)  # Rate-limiting to avoid hitting API limits

    file.write('\n]')  # Close the JSON array

print("Results have been saved to spam_results.json.")
