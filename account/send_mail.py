from django.core.mail import send_mail

HOST = 'localhost:8000'


def send_confirmation_email(user, code):
    link = f'http://{HOST}/api/v1/accounts/activate/{code}/'
    msg = f'Здраствуйте, актривируйте ваш аккаунт!\nЧто бы активировать ваш аккаунт нужно перейти по ссылки ниже:\n{link}\nСсылка работает один раз!'

    send_mail(
        subject='from me',
        message=msg,
        from_email='detskiymir0101@gmail.com',
        recipient_list=[user],
    )