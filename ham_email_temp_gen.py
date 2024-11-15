import json
import re
import random
import pyperclip  # Install with `pip install pyperclip`

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

# Function to create a random possibility of the email
def generate_random_email(template):
    pattern = r"\{(.*?)\}"
    def select_random(match):
        options = match.group(1).split('|')
        return random.choice(options)
    
    return re.sub(pattern, select_random, template)

# Infinite loop to generate emails and get user input
while True:
    email = generate_random_email(EMAIL_TEMPLATE)
    pyperclip.copy(email)  # Copy the email to the clipboard
    print("A new email version has been copied to your clipboard. Respond with '0' to save, or '1' to skip.")
    
    response = input("Enter your response (0 to save, 1 to skip, 'exit' to quit): ").strip()
    
    if response.lower() == 'exit':
        break
    elif response == '0':
        # Append the email to the JSON file
        try:
            with open('email_template.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"emails": []}
        
        data["emails"].append(email)
        
        with open('email_template.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        print("Email saved.")
    elif response == '1':
        print("Email skipped.")
    else:
        print("Invalid input. Please enter '0', '1', or 'exit'.")
