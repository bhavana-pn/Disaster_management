import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

api_key="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"

def send_mail():
    message = Mail(
        from_email='mukesh.yerra@gmail.com',
        to_emails='pnbhavanareddy@gmail.com',
        subject='High chances of forest fire',
        html_content='<strong> High chances of Forest fire </strong>')
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)