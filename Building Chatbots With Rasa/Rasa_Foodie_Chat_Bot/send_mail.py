from flask import Flask
from flask_mail import Mail, Message
import os
import re
app = Flask(__name__)

mail_settings = {
"MAIL_SERVER": 'smtp.gmail.com', 
    "MAIL_USE_TLS": False, #Transport Layer Security
    "MAIL_USE_SSL": True,  #Secure Sockets Layer
    "MAIL_PORT": 465,          #For using SSL
    "MAIL_USERNAME": 'xxxx.xxxx@gmail.com',
    "MAIL_PASSWORD": 'some_password_need_modification'
    }
app.config.update(mail_settings)
mail = Mail(app)


def validate_email(email):
    # regex = r"[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}"
    regex = r"[a-z0-9!#$%&'*+/=?^_‘{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_‘{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    if(re.search(regex,email)):  
        return True  
    else:  
        return False


def mail_results(emailids, html_msg):
    print(emailids)

    for email in emailids:
        # rex = r"(mailto:){0,1}([a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3})"
        rex = r"(mailto:){0,1}([a-z0-9!#$%&'*+/=?^_‘{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_‘{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"
        addresses = re.findall(rex, email)
        print(addresses)
        addresses = list(set([_v[1].replace("|", "") for _v in addresses if validate_email(_v[1])]))

    with app.app_context():
        msg = Message(sender=app.config.get("MAIL_USERNAME"),recipients=addresses)
        msg.subject = "Foodie search results"
        msg.html = html_msg
        mail.send(msg)
        print("email sent!")
