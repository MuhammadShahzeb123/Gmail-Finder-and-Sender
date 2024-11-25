from functions import *


with open('./pages/emails_new.txt', 'r', encoding= 'utf-8') as f:
    emails = f.readlines()

with open("email_template.json", 'r') as f:
    email_templates = json.load(f)


break_point = 20

email_selected = int(random.randint(0, 9))

i = 0

while emails:
    with open('./pages/emails_new.txt', 'r', encoding= 'utf-8') as f: # Read an Email 
        sent_to_email = f.readline().strip()
        f.close()
    chosen_email_by_random = random.randint(0, 5)
    randomized_email = email_template = email_templates['emails'][chosen_email_by_random]
    subject_line = get_random_subject_line()
    try:
        if verify_email(sent_to_email) == True:
            email_sent, sender_email = send_email(sent_to_email, subject_line, randomized_email, email_selected)
        else:
            print(f"{sent_to_email} is invalid")
            email_sent = False
            print(f"Email wasn't sent to {sent_to_email} with the template of email {chosen_email_by_random} because it was invalid")
            update_email_list("./pages/emails_new.txt")
            continue


    except:
        sleep(10)
        email_selected += 1
        subject_line = get_random_subject_line()
        randomized_email = email_template = email_templates['emails'][chosen_email_by_random]
        if verify_email(sent_to_email) == True:
            email_sent, sender_email = send_email(sent_to_email, subject_line, randomized_email, email_selected)
        else:
            print(f"{sent_to_email} is invalid")
            email_sent = False
            print(f"Email wasn't sent to {sent_to_email} with the template of email {chosen_email_by_random} because it was invalid")
            update_email_list("./pages/emails_new.txt")
            continue

    if email_sent is True:
        print(f"Email sent to {sent_to_email} with {sender_email} with the template of email {chosen_email_by_random}")

    else:
        print(f"Email wasn't sent to {sent_to_email} with {sender_email} with the template of email {chosen_email_by_random}")
        i -= 1
    i += 1
    update_email_list("./pages/emails_new.txt")
    email_selected += 1
    if email_selected >= 9:
        email_selected = 0
    
    if i == break_point:
        break
    
    sleep(random.randint(8, 15))
    # if email_sent is True:
    #     # Append the email to the JSON file
    #     try:
    #         with open('email_template.json', 'r') as file:
    #             data = json.load(file)
    #     except (FileNotFoundError, json.JSONDecodeError):
    #         data = {"emails": []}
        
    #     data["emails"].append(randomized_email)
        
    #     with open('email_template.json', 'w') as file:
    #         json.dump(data, file, indent=4)
        
    #     print("Email saved.")
    # elif email_sent is False:
    #     print("Email skipped.")