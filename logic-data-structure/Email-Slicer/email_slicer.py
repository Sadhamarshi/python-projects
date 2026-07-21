class EmailSlicer:

    def __init__(self, email):
        self.email = email

    def slice_email(self):

        if "@" not in self.email:
            print("Invalid Email Address!")
            return

        username, domain = self.email.split("@")

        print("\n===== EMAIL DETAILS =====")
        print(f"Username : {username}")
        print(f"Domain   : {domain}")