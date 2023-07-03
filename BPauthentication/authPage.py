from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import User, Codes
from werkzeug.security import generate_password_hash, check_password_hash
from models import db
from flask_login import login_user, login_required, logout_user
from datetime import date, datetime



authPage = Blueprint('authPage', __name__, static_folder='static', template_folder='templates')

#/*************************  INICIAR SESION  ********************/
@authPage.route('/login')
def login():
    return render_template('login.html')


@authPage.route('/loginPost', methods=['POST'])
def loginPost():

    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    

    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details.')
        return redirect(url_for('authPage.login'))

    login_user(user, remember=remember)
    return redirect(url_for('appPage.home'))

 




#/*************************  REGISTRARSE  ********************/

@authPage.route('/signup')
def signup():
    return render_template('signup.html')



@authPage.route('/signupPost', methods=['POST'])
def signupPost():
    
    email = request.form['email']
    name = request.form['name']
    business = request.form['business']
    password = request.form['password']
    passwordRepeat = request.form['passwordRepeat']
    codeConfi = request.form['codeConfi']
    dates = datetime.now()
    print('datos recividos: {}, {}, {}, {}, {}'.format(email, name, password, passwordRepeat, codeConfi))

    if email == '' or name == '' or business == '' or  password == '' or passwordRepeat == '' or codeConfi == '':
        flash('All fields are required')
        return redirect(url_for('authPage.signup'))

    if password != passwordRepeat :
        flash('passwords are different')
        return redirect(url_for('authPage.signup'))    
        
    user = User.query.filter_by(email=email).first()   
    if user: 
        flash('Email already exists :)')
        return redirect(url_for('authPage.signup'))

    user = User.query.filter_by(business=business).first()   
    if user: 
        flash('Business already exists :)')
        return redirect(url_for('authPage.signup'))
    
  
    code = Codes.query.filter_by(codes=codeConfi).first()    
    if not code or code.states == 1:
        flash('check the code')
        return redirect(url_for('authPage.signup'))      
    code.states = 1
    db.session.commit()

    userTipe = code.types

    user_new = User(email=email, 
                    business=business, 
                    password=generate_password_hash(password), 
                    name=name, codeConfi=codeConfi, 
                    userTipe=userTipe,
                    dates=dates)

    db.session.add(user_new)
    db.session.commit()

    import smtplib
    from email.mime.text import MIMEText

    username = 'inggeodev'
    password = '01111988monita'

    message = MIMEText('Hola!\nEste es un e-mail enviando desde www.inggeodev.com, Usuario registrado\n{}\n{}\n{}\n{}\n{}\n{}'.format('_'*30,email, business, name, codeConfi,userTipe))
    message['From']='inggeodev@gmail.com'
    message['To']='inggeodev@gmail.com'
    message['Subject']='✅ IMPORTANT:  ✉ !Cliente registrado ✉  🌎'    

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(message['From'], message['To'], message.as_string())
    server.quit()

    message = MIMEText('Hola {}!\n\nGracias por registrase a inggeo-proy de inggeodev\npara realizar la activación ingresa a:\n\nvisitar www.inggeodev.com '.format(name,))
    message['From']='inggeodev@gmail.com'
    message['To']=email
    message['Subject']='✅ Activación 👷 INGGEODEV 👷'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(message['From'], message['To'], message.as_string())
    server.quit()


    return redirect(url_for('authPage.login'))

#/*************************  CERRAR SESION  ********************/
@authPage.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('indexPage.index'))