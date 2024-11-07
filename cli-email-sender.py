from functions import *

EMAIL = """
Hi

{If you’re in the service business then Guess what? you can ditch the outreach and ads to get clients now!|I've got some awesome news! If you’re running a service-based business, you don’t need to stress about outreach or ads to get clients anymore.|Big news! If you run a service business, you don’t have to deal with outreach or ads for clients anymore.|Quick heads-up: If you run a service-based biz, you can forget about outreach and ads for getting clients!|Skip the ads, skip the outreach. Here’s the smart way to land clients.|Tired of spending hours on client outreach with limited results? There’s a better way now with AI!|Imagine if getting new clients for your service-based business didn’t require constant outreach!|Ever thought there could be a simpler way to bring in clients without endless outreach?|Tired of the slow, manual hustle for new clients? An AI Automated approach might change everything.|Running a service business can feel like a grind when it comes to finding clients, right? But what if there’s a new way to speed that up?|It’s no secret that finding clients can be a slow process. What if you could make it easier with a fresh approach?|Reaching new clients can sometimes feel like a slow climb, can’t it? Here’s a thought—AI could lighten the load.|If growing your client list has been a challenge, you might want to hear about a new possibility.|You’ve likely noticed how time-consuming outreach can be for a service business. Here’s an approach that might shake things up.}

{I've developed a tool that will scrape the leads, write the Emails and send them automatically, Automatically!|Hey, I’ve created a tool that handles everything—finding leads, writing emails, and sending them out, all on autopilot.|You’re gonna love this—I built a tool that finds leads, writes emails, and sends them automatically. You don’t have to do a thing!|I’ve come up with a tool that’ll take care of everything—finding leads, writing emails, and sending them, all by itself!|Imagine a tool that does it all: finds the right leads, crafts the emails, and sends them out—completely automated.|I’ve built a tool that takes care of everything for you—from finding leads to writing and sending emails—all automatically.|With my new tool, the entire outreach process is handled for you—finding, writing, and sending emails, all in one.|I’ve designed a tool that takes over the outreach process, using AI to find leads, craft messages, and send them out automatically using AI.|Think about having a tool that finds the clients you need, writes the perfect emails, and sends them—all without you lifting a finger.|This tool does the heavy lifting: finds your leads, writes the emails, and sends them—completely on autopilot.|I’ve built a tool that turns outreach into a hands-off process, automatically finding leads, drafting messages, and sending them.|Picture a tool that takes over the entire client outreach process, finding leads and sending emails, fully automated.}

{As soon as someone replies, the AI steps in, replies back, nurtures the lead, and keeps things moving toward booking a call.|The AI tracks replies and automatically sends a response, handling lead nurturing for you—calls get booked without you doing a thing|If someone replies to your email, the AI tracks it, replies automatically, nurtures the lead, and helps you book calls seamlessly|Replies are handled by the AI—it automatically responds, nurtures the lead, and works to book calls, all while you focus on other things.|When someone replies, the AI steps in to handle everything—tracking responses, nurturing leads, and guiding them to book a call.|The AI checks for replies regularly, responds instantly, nurtures the lead, and helps move things toward an appointment, all on autopilot.|Once a lead responds, the AI takes over, replying, nurturing the conversation, and working toward booking a call for you.|Every reply is automatically managed by the AI, which responds, nurtures the lead, and guides them seamlessly toward an appointment.|The AI steps in with every reply, responding, nurturing, and setting up appointments, so you’re free to focus on other areas.|Any reply is captured by the AI, which takes care of follow-ups, lead nurturing, and guiding them toward a call—all hands-free.|Each lead reply is managed by AI, responding promptly, nurturing the relationship, and steering them to book a call without any manual work.}

{So, all that’s left for you to do is hop on a call, close the client, and watch the cash roll in. I’ve got everything else covered|All you’ve gotta do is take the call, seal the deal, and the money’s yours. I’m taking care of everything else|You handle the call and close the deal—that’s it! I’m taking care of everything else so you can just focus on making money.|All you have to worry about is closing the client on the call, then sit back and make money. I’ve already done all the hard work!|All that’s left for you is to jump on the call, close the deal, and start bringing in revenue. Everything else is handled.|Just focus on the calls and securing your clients—I’ve already set up the system to do the rest for you.|Your only task is to close the deal on the call. I’ve taken care of everything else so you can focus on growing your business.|With everything automated, all you need to do is show up, close the client, and see the profits come in.|I’ve set up the whole process—just focus on the call and turning leads into clients, while the tool manages everything else.|All you have to do is get on the call and secure the client. I’ve done the groundwork to ensure your pipeline is always full.|The tool handles every step, so you only need to take the calls and lock in your clients—simple and effective.|All you have to do is jump on the calls and close. I’ve created the process so you can focus entirely on delivering to your clients.|Everything is ready for you to just take the call and bring in the business. The rest is handled on autopilot.}

{Funny thing is, I didn’t even send you this email—the system I built did it for me! It found your business and sent this automatically.|Here’s the crazy part—I didn’t actually send you this email. My system did, all by itself, after finding your business in the niche I set!|Believe it or not, this email came from the system I built, not me! It found your business and sent this message on its own|The best part? I didn’t even send this email myself—my system found your business and reached out automatically!|Here’s the kicker—I didn’t send this email. The system I built did, after identifying your business as a match!|Believe it or not, this email came to you automatically through the tool I created. It found and reached out to your business on its ow|Crazy as it sounds, I didn’t send you this email—my AI system did! It found your business and sent this message without my input.|What’s amazing is that my system sent you this email by itself, after automatically finding your business in the ideal niche.|Hard to believe, but this email wasn’t even from me—my system found your business and handled the rest on its own.|Here’s the twist: my system sent this email, not me! It found your business and handled the outreach without me lifting a finger.|Here’s the real surprise—I’m not the one who sent this email! My system found your business and reached out all on its own.|Funny thing, I’m not the one who sent you this email—my automated system did. It identified your business and reached out independently!}

{If you reply to this email, just know the AI will respond and guide you to book a call—so save yourself the time and just book a call directly|FYI, if you reply to this email, the AI will respond and direct you to book a call. You can skip all that and just book it now!|Replying will get an AI response telling you to book a call, so save the time and hassle—just book it right from here|If you reply, you'll be chatting with an AI that will simply guide you to book a call—let's save time and book directly!|Any reply to this email will get an automated AI response nudging you to book a call, so let’s cut to the chase and book now.|The AI will answer any reply, redirecting you to book a call anyway, so go ahead and reserve your time now!|Just so you know, replying to this email connects you to an AI that will guide you to schedule a call—skip the extra steps and book now!|This email is automated, and any reply will only lead you to a call booking prompt. Why wait? Go ahead and book now.|If you hit “reply,” you’ll reach an AI that will suggest you book a call anyway—let’s make it easier and book directly!|Be aware that replies will connect you to an AI that will prompt you to book a call. Get ahead and secure your slot now!|Any response will be met with an AI suggesting you book a call—so let’s keep it simple and schedule a time right away.|I won't reply 'cause replying will connect you to an my AI that will guide you to book a call—save time and schedule directly!}

{Here you go: https://calendly.com/zcops/auto-ai-outreach |Book the Call Here: https://calendly.com/zcops/auto-ai-outreach |Simple Click here: https://calendly.com/zcops/auto-ai-outreach|Take the Lead—Book Your Call Now: https://calendly.com/zcops/auto-ai-outreach|Own It—Reserve Your Time: https://calendly.com/zcops/auto-ai-outreach|Claim Your Time Here: https://calendly.com/zcops/auto-ai-outreach|Take the Next Step—Book Here: https://calendly.com/zcops/auto-ai-outreach|Show Initiative—Schedule Now: https://calendly.com/zcops/auto-ai-outreach|Go for It—Lock in Your Call: https://calendly.com/zcops/auto-ai-outreach}

{Best. Looking forward to meeting with ya!|Can’t wait to connect with you soon!|Looking forward to an awesome convo!|Excited to meet—see you soon!|Looking forward to our chat—let’s make it great!|Ready to connect—see you soon!|Excited to chat—see you there!|Let’s make it a productive one—looking forward to it!}


Shahzeb Naveed
CEO
ZCopS

P.S: {I’m developing AI that will locate the exact business emails you need, gather lead-specific insights, and write personalized emails—all without my input.|Soon, my AI will automatically find the right business contacts, gather personal insights, and create targeted emails that stand out.|I'm adding features that will enable the AI to find professional emails, collect recent lead insights, and tailor messages that make a real impact.|Coming up: my AI will source business contacts, gather personalized info, and write each email with current insights on your leads.|Next up: an AI that autonomously finds business emails, pulls recent events, and crafts emails that resonate with each unique contact.|My upcoming AI tool will identify business emails, pull detailed lead data, and create one-of-a-kind, personalized outreach for you.|I’m building AI that locates professional contacts, gathers personal lead insights, and writes custom emails that make a lasting impression.|My new AI will soon be able to find professional contacts, scrape timely lead info, and generate hyper-personalized emails automatically.|The next upgrade will let my AI locate business emails, gather fresh insights on each lead, and craft emails tailored just for them.|Soon, my AI will not only locate business contacts but also collect recent lead info to craft customized, relevant emails that truly connect.}
"""


with open('./pages/emails.txt', 'r', encoding= 'utf-8') as f:
    emails = f.readlines()
    
break_point = 100

email_selected = 0

i = 0

while emails:
    
    with open('./pages/emails.txt', 'r', encoding= 'utf-8') as f: # Read an Email 
        sent_to_email = f.readline().strip()
        f.close()

    subject_line = get_random_subject_line()
    
    randomized_email = change_email_msg(EMAIL)
    email_sent, sender_email = send_email(sent_to_email, subject_line, randomized_email, email_selected)
    if email_sent is True:
        print(f"Email sent to {sent_to_email} with {sender_email}")
    else:
        print(f"Email wasn't sent to {sent_to_email} with {sender_email}")
    update_email_list("./pages/emails.txt")
    sleep(random.randint(5, 10))
    i += 1
    if i == 250:
        if email_selected == 0:
            email_selected = 1
        elif email_selected == 1:
            email_selected = 2
        elif email_selected == 2:
            email_selected = 0
    
    if i == break_point:
        break