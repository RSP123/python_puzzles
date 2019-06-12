# This programs for email validation

import re # Calling RE package

# Function to check email
def email_check(email):
    if re.match("^(.@)[a-zA-Z][0-9].com$", email):    # RE Matchs for . , @ , [a-zA_Z0-9]
        if re.match("^[\s](^ $ * + ? {} () \ |)",email):
        # RE Matchs for otherspecial character in email id 
            return False
        return True
    return False


# Main

if __name__ =="__main__":
    email=str(input("Enter a email id :")) # User input
    if email_check(email):
        print("The given email id is VALID")
    else:
        print("The given email id is not VALID !")
