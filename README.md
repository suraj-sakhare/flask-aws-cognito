# Flask AWS Cognito App

A simple Flask application integrated with AWS Cognito for user authentication. This app allows users to log in and out using their AWS Cognito credentials.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication via AWS Cognito
- Login and logout functionality
- Simple HTML front-end
- Environment variable management for secure credential storage

## Requirements

- Python 3.6 or higher
- Flask
- Requests
- Python-dotenv
- Python-JOSE

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-flask-app.git
   cd your-flask-app/src

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv

   On Windows : venv\Scripts\activate
   On macOS/Linux : source venv/bin/activate

3. **Install the required dependencies:**  

   ```bash
   pip install -r requirements.txt
 

## Configuration

1. **Create a .env file in the src/ directory and add your AWS Cognito configuration details:**

- COGNITO_POOL_ID = your_cognito_pool_id  # e.g., us-east-1_example
- COGNITO_CLIENT_ID = your_cognito_client_id  # e.g., 3n2abcde4fg5hijklmno
- COGNITO_CLIENT_SECRET= your_cognito_client_secret  # Leave empty if no secret
- COGNITO_DOMAIN = your_cognito_domain  # e.g., my-cognito-domain
- REDIRECT_URI = https://your-redirect-url.com  # Change to your actual redirect URL

Additional
- LOGIN_URL = 
- TOKEN_URL = 
- COGNITO_LOGOUT_URL = 


## Usage

1. **Run the application:**

   python app.py

2. **Visit the application in your browser:** 

   Navigate to http://127.0.0.1:5000/ in your web browser.

3. **Login:**

   Click the "Login with Cognito" button to authenticate using AWS Cognito.

4. **Logout:**

   After logging in, you will see a logout button to exit the session.


## File Structure 

    TEST-AWS-COGNITO/
    │
    ├── src/
    │   ├── templates/
    │   │   └── home.html           # HTML template file for home page
    │   ├── static/
    │   │   └── style.css           # (Optional) CSS files
    │   ├── config.py               # Configuration file for loading environment variables
    │   ├── app.py                  # Main Flask application file
    │   └── .env                    # Environment variables (not pushed to the repo)
    │
    ├── .gitignore                   # Git ignore file
    ├── README.md                    # Project README file
    ├── requirements.txt             # Python dependencies
    └── venv/                        # Virtual environment (optional)

## Contributing

- Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.

