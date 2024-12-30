from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/location', methods=['POST'])
def get_location():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']

    # Send email
    send_email(latitude, longitude)

    return jsonify({"message": "Location received and email sent!"}), 200

def send_email(latitude, longitude):
    sender = "cletocite@gmail.com"
    receiver = "cletocite.techs@gmail.com"
    password = "dxkbhzyaqaqcgrrq"

    subject = "User Location"
    body = f"User's location: Latitude {latitude}, Longitude {longitude}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

if __name__ == '__main__':
    app.run(debug=True)