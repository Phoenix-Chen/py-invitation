from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Invitation:
    def __init__(self):
        """Handler for invitation.

            Attributes:
                smtp_conn (object) : A smtplib.SMTP object.
                email_addr (str) : SMTP host email.

        """
        self.smtp_conn = None
        self.email_addr = None

    def set_smtp(self, host, port, host_user, host_password, use_tls=True):
        """Setup SMTP connection.

            Args:
                host (str) : SMTP server host.
                port (int) : SMTP port.
                host_user (str) : SMTP host email.
                host_password (str) : SMTP host password.
                use_tls (boolean, optional) : Whether the SMTP uses TLS. Defaults to True.

        """
        self.smtp_conn = SMTP(host, port=port)
        #self.smtp_conn.set_debuglevel(False)
        if use_tls:
            self.smtp_conn.starttls()
        self.smtp_conn.login(host_user, host_password)
        self.email_addr = host_user


    def send(self, receiver_email, template):
        """Send the invitation.

            Args:
                receiver_email (str) : The email address of receiver.
                template (object) : A py_invitation.Template object.

        """
        # FIXME: Check if template isinstance(Template) and raise an error if not
        self.smtp_conn.sendmail(self.email_addr, receiver_email, template.to_string())

    def close(self):
        """Close the smtp connection.
        """
        self.smtp_conn.quit()
