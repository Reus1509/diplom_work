from flask import Flask, request, render_template
from db.models import db, User
from app import send_mail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.secret_key = "qweasdzxcqweasdzxc123@#!#"
db.init_app(app)


@app.get("/")
def main_page():
    return render_template("login_form.html")

@app.post("/signup/")
def sign_up_post():
    login = request.form['login']
    email = request.form['email']
    password = request.form['password']

    user = User(user_login=login, user_email=email, user_password=password)
    db.session.add(user)
    db.session.commit()
    send_mail.main()
    print("На вашу почту отправлено сообщение!")
    return render_template('login_form.html')


@app.post("/signin/")
def sign_in():
    pass


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
