# py-invitation
***
A simple Python library for sending email invitation with HTML or plain text.

## Install
***
- To install. Run:
    ```bash
    pip install git+https://github.com/Phoenix-Chen/py-invitation.git
    ```

## Usage
***

### Setup html template

Edit your HTML template or plain text to include `variables` in the format of `{{VARIABLE_NAME}}`:

```html
    Dear {{receiver_name}}:
    <a href="{{callback_url}}"> RSVP Now </a>
```

### Setup template
```python
    from py_invitation import Template

    template = Template(EMAIL_SUBJECT, SENDER_EMAIL, RECEIVER_EMAIL)

    # Create confirmation token (recommand to use a random token)
    token = base64.b32encode(os.urandom(10)).decode('utf-8') # You probably want to save the token into your database for later verification

    # Make variables
    variables = {
        'callback_url': "www.your_site.com/verify?code=" + token,
        'receiver_name': RECEIVER_NAME
    }

    # Load into template
    template.load_template_from_file("./templates/invitation2.html", variables)

    # Add attachment
    template.add_attachment("./invitation.png")
```

### Send invitation
```python
    from py_invitation import Invitation

    invitation = Invitation()
    invitation.set_smtp(EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    invitation.send(RECEIVER_EMAIL, template)
    invitation.close()
```


## Documentation
***

## Invitation
```python
Invitation(self)
```
Handler for invitation.

#### Attributes:
- smtp_conn (`object`) : A smtplib.SMTP object.
- email_addr (`str`) : SMTP host email.


### set_smtp
```python
Invitation.set_smtp(self, host, port, host_user, host_password, use_tls=True)
```
Setup SMTP connection.

#### Args:
- host (`str`) : SMTP server host.
- port (`int`) : SMTP port.
- host_user (`str`) : SMTP host email.
- host_password (`str`) : SMTP host password.
- use_tls (`boolean`, optional) : Whether the SMTP uses TLS. Defaults to True.


### send
```python
Invitation.send(self, receiver_email, template)
```
Send the invitation.

#### Args:
- receiver_email (`str`) : The email address of receiver.
- template (`object`) : A py_invitation.Template object.


### close
```python
Invitation.close(self)
```
Close the smtp connection.



## Template
```python
Template(self, subject, sender, receiver)
```
Template contains all the email info.

#### Args:
- subject (`str`) : Subject of the email.
- sender (`str`) : The email address of sender.
- receiver (`str`) : The email address of receiver.

#### Attributes:
- msg (`object`) : A email.mime.multipart.MIMEMultipart object.


### load_template_from_str
```python
Template.load_template_from_str(self, template_str, variables, is_html=False)
```
Load email body from string.

#### Args:
- template_str (`str`) : HTML string or plain text as email body.
- variables (`dict(str)`) : A dictionary containing all the variables to be replaced in template.
- is_html (`boolean`, optional) : Whether the string is HTML. Defaults to False.


### load_template_from_file
```python
Template.load_template_from_file(self, template_path, variables, is_html=False)
```
Load email body from a file.

#### Args:
- template_path (`str`) : Path to the html or text message as email body.
- variables (`dict(str)`) : A dictionary containing all the variables to be replaced in template.
- is_html (`boolean`, optional) : Whether the file is HTML. Defaults to False.


### add_attachment
```python
Template.add_attachment(self, file_path)
```
Add an attachment to the email.

#### Args:
- file_path (`str`) : Path to the attachment.


### to_string
```python
Template.to_string(self)
```
Returns email info as a string.

#### Returns:
- `str` : Info about email as a string.
