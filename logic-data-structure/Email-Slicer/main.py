from email_slicer import EmailSlicer


print("===== EMAIL SLICER =====")

email = input("Enter Email Address: ")

slicer = EmailSlicer(email)

slicer.slice_email()