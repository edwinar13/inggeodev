
from flask import Blueprint, render_template, redirect, url_for, request


indexPage = Blueprint('indexPage', __name__, static_folder='static', template_folder='templates')

@indexPage.route('/')
def index():
    return render_template('index.html')


@indexPage.route('/contactPost', methods=['POST'])
def contactPost():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    message = request.form.get('message')

    username = 'inggeodev'
    password = '01111988monita'

    import smtplib
    from email.mime.text import MIMEText

    message = MIMEText('Hola!\nEste es un e-mail enviando desde www.inggeodev.com \n{}\n{}\n{}\n{}\n{}'.format('_'*30,name, phone, email, message))
    message['From']='inggeodev@gmail.com'
    message['To']='inggeodev@gmail.com'
    message['Subject']='🔴 IMPORTANT:  😀  !Cliente nuevo¡ 😀🎊🎉'

    

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(message['From'], message['To'], message.as_string())
    server.quit()

    message = MIMEText('Hola {}!\n\nGracias por preferir a inggeodev\npronto no pondremos en contacto\n\nRecuerda visitar www.inggeodev.com '.format(name,))
    message['From']='inggeodev@gmail.com'
    message['To']=email
    message['Subject']='🎊 Bienvenido a 👷 INGGEODEV 👷'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(message['From'], message['To'], message.as_string())
    server.quit()

    return redirect(url_for('indexPage.index'))

