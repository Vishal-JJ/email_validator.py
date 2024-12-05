import re

def is_valid_email(email):
    # Define the regex pattern for a valid email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Use re.match to check if the email matches the pattern
    return re.match(pattern, email) is not None

# Test the function
while 1>0:
      email = input("Enter an email address: ")
      if is_valid_email(email):
           print("Valid email.")
      else:
            print("Invalid email.")
