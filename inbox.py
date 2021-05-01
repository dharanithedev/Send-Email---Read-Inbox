import imaplib
import email

# iMapServer
iMapHost = 'imap.gmail.com'
# Credentials
username, password = 'dharani.python@gmail.com', 'xxxxxxx'

def get_inbox():
    mail = imaplib.IMAP4_SSL(iMapHost)
    mail.login(username, password)
    mail.select("inbox") #Target folder
    _, search_data = mail.search(None, 'UNSEEN') #search only unread emails

    unreadEmails = []

    for data in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(data, '(RFC822)') #STANDARD FOR THE FORMAT OF ARPA INTERNET TEXT MESSAGES
        _, x = data[0]
        email_message = email.message_from_bytes(x)

        for header in ['subject', 'to', 'from', 'date']:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]

        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                text_body = part.get_payload(decode=True)
                email_data['body'] = text_body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()    

        unreadEmails.append(email_data)

    return unreadEmails

if __name__ == "__main__":
    my_inbox = get_inbox()
    for e in my_inbox:
        print(e)


