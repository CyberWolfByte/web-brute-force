# Web Login Brute Force (WebGoat)

This Python script executes a brute force attack on a web application's login page by trying different combinations of usernames and passwords. It targets the WebGoat application's login page, cycling through a list of usernames and a wordlist of passwords to find valid credentials. The script sends POST requests for each username-password pair, searching for a successful login indicator in the response. Upon finding a match, it outputs the successful credentials and exits. If no match is found for a username, it moves to the next. The process includes real-time feedback on the attempts being made.

## Disclaimer

The tools and scripts provided in this repository are made available for educational purposes only and are intended to be used for testing and protecting systems with the consent of the owners. The author does not take any responsibility for the misuse of these tools. It is the end user's responsibility to obey all applicable local, state, national, and international laws. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Under no circumstances should this tool be used for malicious purposes. The author of this tool advocates for the responsible and ethical use of security tools. Please use this tool responsibly and ethically, ensuring that you have proper authorization before engaging any system with the techniques demonstrated by this project.

## Features

- **Automated Login Attempts**: The script automates the process of logging into the WebGoat application by cycling through a list of common usernames and passwords.
- **Real-Time Feedback**: Provides immediate feedback on the status of each login attempt, enhancing the user's understanding of the brute force process.
- **Success Detection**: Detects and reports successful login attempts, displaying the valid credentials.
- **Robust Testing Environment**: Specifically designed to interact with WebGoat, an intentionally insecure web application, making it an ideal tool for educational purposes in web security.

## Prerequisites

- **Operating System**: Tested on Kali Linux 2023.4
- **Python Environment**: Requires Python 3.x installed on your system.
- **Required Python Libraries**:
    - `requests`: For sending HTTP requests to the WebGoat server.
    - `sys`: For accessing command-line arguments and system operations.
- **Password List**:
    - Utilizes "10-million-password-list-top-100.txt" for password attempts. Ensure this file is downloaded and accessible in the script's directory.
- **WebGoat Application**:
    - Make sure WebGoat is installed and running locally, as this script targets its login page. Follow the provided installation steps for setting up WebGoat using Docker.

## Installation

Follow these detailed steps to set up the Web Login Brute Force script environment, including the installation of the WebGoat application:

1. **Install Python**: Make sure Python is installed. On Kali Linux, use:
    
    ```bash
    sudo apt-get update
    sudo apt-get install python3
    ```
    
2. **Install Python Libraries**: Install the necessary libraries using pip:
    
    ```bash
    pip install requests
    ```
    
3. **Prepare Password List**: Ensure you have the password list file "10-million-password-list-top-100.txt" in the same directory as your script:
    [SecLists/Passwords/Common-Credentials at master · danielmiessler/SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials)
    
4. **Script Modifications**: Update the script accordingly to reflect your target word list if not using the default.
5. **Set Up WebGoat**: Detailed instructions for setting up WebGoat using Docker are provided. Ensure WebGoat is running correctly before attempting to use the brute force script.

## WebGoat Installation (Docker)

[GitHub - WebGoat/WebGoat: WebGoat is a deliberately insecure application](https://github.com/WebGoat/WebGoat?tab=readme-ov-file)

[Docker](https://hub.docker.com/r/webgoat/webgoat)

To install WebGoat for local testing using Docker, you'll leverage Docker's capability to pull and run images from Docker Hub. WebGoat is an intentionally insecure web application maintained by OWASP, designed for learning and practicing web application security.

1. **Pull the WebGoat Docker Image:** Execute the following command to pull the latest WebGoat Docker image:
    
    ```bash
    sudo docker pull webgoat/webgoat
    ```
    
2. **Run WebGoat Container:** After downloading the image, to run WebGoat without worrying about timezone or proxy settings, use:
    
    ```bash
    sudo docker run -it -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 webgoat/webgoat
    ```
    
    This command runs WebGoat accessible at ports 8080 and 9090 on your local machine, restricting access to your local system only, which is a good security practice.
    
3. **Setting the Timezone:** For lessons that require the container to run in the same timezone as your host system, specify the `TZ` environment variable:
    
    ```bash
    sudo docker run -it -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 -e TZ=America/Chicago webgoat/webgoat
    ```
    
4. **Access WebGoat:** Once the container is running, open your web browser and navigate to:
    
    ```bash
    http://localhost:8080/WebGoat
    ```
    
    You should see the WebGoat login page, where you can register a new user or log in if you've already created a user.
    
5. **Additional Tips:**
    - **Data Persistence**: By default, any data or progress you make in WebGoat will be lost once the Docker container is stopped. To persist data, consider using Docker volumes to save progress outside of the container.
    - **Stopping WebGoat**: To stop the WebGoat container, you can use `docker stop <container_id>` where `<container_id>` is the ID of the WebGoat container. You can find the container ID by running `docker ps`.
    - **Security Consideration**: Remember that WebGoat is designed to be insecure. Do not expose the WebGoat container to the internet or untrusted networks.

## Usage

To use the Web Login Brute Force script against the WebGoat application, follow these instructions:

1. **Start WebGoat**: Ensure that WebGoat is running on your local machine as described in the Installation section.
2. **Run the Brute Force Script**:
    
    ```bash
    python3 web_brute_force.py
    ```
    
3. **Monitor Output**: Watch the terminal for real-time feedback on login attempts. The script will report success if it finds a valid username-password combination.

## How It Works

The script functions through several key operations:

- **Password and Username Iteration**: Iterates through a list of usernames and a separate list of passwords, attempting each combination against the target login page.
- **HTTP POST Requests**: For each username-password pair, a POST request is sent to the WebGoat login endpoint.
- **Success Indicator Detection**: Analyzes the response from each login attempt to check for a predefined success indicator, which confirms a successful login.
- **Output of Results**: If a valid login is detected, the script outputs the successful username and password combination and terminates. If no valid credentials are found for a username, it moves to the next.

## Output Example

```bash
$ python3 web_brute_force.py
[X] Attempting user:password -> admin:minecraft0
        No password found for 'admin'!
[X] Attempting user:password -> user:minecraft0
        No password found for 'user'!
[X] Attempting user:password -> default:qwertyuiop
        [>>>] Valid password 'qwertyuiop' found for user 'default'!
```

## Contributing

If you have an idea for an improvement or if you're interested in collaborating, you are welcome to contribute. Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/CyberWolfByte/web-brute-force/blob/main/LICENSE) file for details.
