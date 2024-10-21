from flask import Flask, redirect, request, session, render_template, url_for
import requests
from jose import jwt
from config import Config 

app = Flask(__name__)
app.config.from_object(Config)

# Generate AWS Cognito Login URL
def get_cognito_login_url():
    login_url = app.config["LOGIN_URL"]
    return login_url

# Route for Login
@app.route('/login')
def login():
    login_url = get_cognito_login_url()
    return redirect(login_url)

# Redirect Route after Login (This will handle the redirection after successful login)
@app.route('/redirect')
def redirect_handler():
    code = request.args.get('code')

    # Exchange the authorization code for tokens
    token_url = app.config["TOKEN_URL"]
    token_data = {
        'grant_type': 'authorization_code',
        'client_id': app.config["COGNITO_CLIENT_ID"],
        'redirect_uri': app.config["REDIRECT_URI"],
        'code': code
    }

    token_headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    token_response = requests.post(token_url, data=token_data, headers=token_headers)
    tokens = token_response.json()

    id_token = tokens.get('id_token')
    if id_token:
        # Verify the JWT token
        cognito_keys = requests.get(app.config["COGNITO_KEYS_URL"]).json()
        decoded_token = jwt.decode(id_token, cognito_keys['keys'], algorithms=['RS256'], audience=app.config["COGNITO_CLIENT_ID"])
        session['username'] = decoded_token['cognito:username']
        
        # Redirect to home with a success message
        return redirect(url_for('home', status='success'))
    else:    
        # Redirect to home with a failure message
        return redirect(url_for('home', status='failure'))


# Route for Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(app.config["LOGOUT_URL"])

# Home Route with Login Button
@app.route('/')
def home():
    user = session.get('username')
    return render_template('home.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
