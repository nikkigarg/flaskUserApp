import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app import db, app
from app.Users.models import User
from datetime import datetime as dt


def add_user(request):
    try:
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')
        new_user = ''
        if email:
            new_user = User(name=name,
                            email=email,
                            password=password,
                            created_on=dt.now(),
                            website="www:http://w3schools.com")
            db.session.add(new_user)  # Adds new User record to database
            db.session.commit()  # Commits all changes
        send_mail()
        return f"{new_user} successfully created!"
    except Exception as e:
        print(e)
        return "Error in creating User"


def edit_user(request, user_id):
    try:
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')
        website = request.json.get('website')
        user = User.query.get(user_id)
        user.name = name,
        user.email = email,
        user.password = password,
        user.created_on = dt.now(),
        user.website = website
        db.session.commit()  # Commits all changes
        return f"{user} updated successfully."
    except Exception as e:
        print(e)
        return "Error in creating User"


def get_user(user_id):
    try:
        user = User.query.get(user_id)
        data = {"name": user.name, "email": user.email, "website": user.website}
        return data
    except Exception as e:
        print(e)
        return {}


def get_all_user():
    try:
        data = []
        users = User.query.all()
        for user in users:
            data.append({"user_id": user.id, "name": user.name, "email": user.email, "website": user.website})
        return {"data": data}
    except Exception as e:
        print(e)
        return {"data": []}


def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return "user deleted successfully."
    except Exception as e:
        print(e)
        return "Error in deleting user"


def send_mail():
    message = MIMEMultipart("alternative")
    message["Subject"] = "Account created successfully"
    message["From"] = app.config.get("MAIL_USERNAME")
    message["To"] = "receiver@gmail.com"

    text = """\
    Hi,
    How are you?
    Your account created successfully."""
    html = """\
    <html>
      <body>
        <p>Hi,<br>
          Your account created successfully.<br> 
        </p>
      </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP_SSL(app.config.get("MAIL_SERVER"), app.config.get("MAIL_PORT")) as server:
        server.login(app.config.get("MAIL_USERNAME"), app.config.get("MAIL_PASSWORD"))
        server.sendmail(app.config.get("MAIL_USERNAME"),
                        "receiver.gmail.com",message.as_string())
