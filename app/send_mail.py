import smtplib
from email.mime.text import MIMEText


def send_email(message):
    sender = "fl.nikita.kuznetsov@yandex.ru"
    # your password = "your password"
    password = "wgfptdcezabgziuh"

    server = smtplib.SMTP("smtp.yandex.ru", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Успешная регистрация!"
        server.sendmail(sender, "nkuz1509@gmail.com", msg.as_string())

        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    message = "Вы успешно зарегистрировались на Киберфарм! Спасибо за регистрацию."
    print(send_email(message=message))
