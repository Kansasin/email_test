import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    user = "kostyazinovev9@gmail.com"
    password = "ljwzoaeolnlhpujb"

    msg = EmailMessage()
    msg.set_content(body, subtype="html", charset='utf-8')
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


def main():
    body = ''
    with open('index.html', encoding='utf-8') as f:
        body = f.read()
    email_alert('Test', body, 'fominigor435@gmail.com')


if __name__ == "__main__":
    main()
