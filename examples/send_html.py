import os
import base64
from py_invitation import Invitation, Template


# Setup template
template = Template(EMAIL_SUBJECT, SENDER_EMAIL, RECEIVER_EMAIL)

# Create confirmation token (recommand to use a random token)
token = base64.b32encode(os.urandom(10)).decode('utf-8') # You probably want to save the token into your database for later verification

# Make variables
variables = {
    'callback_url': "www.your_site.com/verify?code=" + token
}

# Load into template
template.load_template_from_file("./examples/templates/invitation2.html", variables, is_html=True)


# Setup invitation
invitation = Invitation()
invitation.set_smtp(EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
invitation.send(RECEIVER_EMAIL, template)
invitation.close()
