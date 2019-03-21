from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Template:
    def __init__(self, subject, sender, receiver):
        """Template contains all the email info.

            Args:
                subject (str) : Subject of the email.
                sender (str) : The email address of sender.
                receiver (str) : The email address of receiver.

            Attributes:
                msg (object) : A email.mime.multipart.MIMEMultipart object.

        """
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = subject
        self.msg['From'] = sender
        self.msg['To'] = receiver


    def load_template_from_str(self, template_str, variables):
        """Load email body from string.

            Args:
                template_str (str) : HTML string or plain text as email body.
                variables (dict(str)) : A dictionary containing all the variables to be replaced in template.

        """
        # FIXME: Redo the variable replacement to handle {{{{key_1}}}} where {{key_1}} = key_2
        for key, value in variables.items():
            pattern = '{{' + key + '}}'
            template_str = template_str.replace(pattern, value)
        self.msg.attach(MIMEText(template_str, 'html'))


    def load_template_from_file(self, template_path, variables):
        """Load email body from a file.

            Args:
                template_path (str) : Path to the html or text message as email body.
                variables (dict(str)) : A dictionary containing all the variables to be replaced in template.

        """
        try:
            f = open(template_path, "r")
            self.load_template_from_str(f.read(), variables)
            f.close()
        except Exception as e:
            print(e)


    def add_attachment(self, file_path):
        """Add an attachment to the email.

            Args:
                file_path (str) : Path to the attachment.

        """
        try:
            f = open(file_path, "rb")
            part = MIMEApplication(
                f.read(),
                Name=basename(file_path)
            )
            f.close()
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file_path)
            self.msg.attach(part)
        except Exception as e:
            print(e)


    def to_string(self):
        """Returns email info as a string.

            Returns:
                str : Info about email as a string.

        """
        return self.msg.as_string()
