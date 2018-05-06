import poplib
import email.policy
import email
from email.header import *
import os
from datetime import *

SERVER  =[] #bitte ausfüllen
USER    =[]
PASSWORD=[]

MAILS = []

for i in range(0, len(SERVER)):
    Mailbox = poplib.POP3_SSL(SERVER[i], '995')
    Mailbox.user(USER[i])
    Mailbox.pass_(PASSWORD[i])

    numMessages = int(len(Mailbox.list()[1]))
    i = int(len(Mailbox.list()[1]))

    while i != 0 and i > int(numMessages - 4):
        raw_email  = b"\n".join(Mailbox.retr(i)[1])
        parsed_email = email.message_from_bytes(raw_email, policy=email.policy.default)

        date = parsed_email.get('date').datetime
        date = date.strftime("%Y %m %d %H:%M")

        subject = decode_header(parsed_email['Subject'])
        subject = subject[0][0]

        try:
                subject = str(subject).split("'")[1]
        except:
                pass

        MAILS.append(str(date) + "##::##" + str(subject))

        i = i - 1

    Mailbox.quit()

MAILS = sorted(MAILS)
i = 0
numMessages = len(MAILS)
text = ""

while i != numMessages and i < 4:
    text = text + MAILS[i].split("##::##")[1] + "\n"
    i = i + 1

with open("RAM/Mail.txt", "w") as out:
    out.write(text)
    os.system("touch RAM/refresh")
    out.close()
