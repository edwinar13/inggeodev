
import os
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db, UserSchema, User, ProjectsSchema, Projects
from werkzeug.utils import secure_filename
from datetime import date, datetime

appPage = Blueprint('appPage', __name__, static_folder='static', template_folder='templates')


@appPage.route('/home')
@login_required
def home():  
    user_schema = UserSchema()
    users_schema = UserSchema(many = True)

    users = User.query.all()
    #print(users)
    result = user_schema.dump(users[0])
    #print(result)
    result = users_schema.dump(users)
    #print(result)

    projects = Projects.query.all() 
    projectsSchema = ProjectsSchema(many = True)
    datos = projectsSchema.dump(projects)  
    
    return render_template('home.html', name = current_user.name, email = current_user.email, registros=datos)



@appPage.route('/uploadDoc', methods=['POST'])
@login_required
def uploadDoc():
    if request.method == 'POST':
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join('.\\Archivos_PDF', filename))
    # Retornamos una respuesta satisfactoria
    return "<h1>Archivo subido exitosamente</h1>"






@appPage.route('/newProjectPost', methods=['POST'])
@login_required
def newProjectPost():    
    name =request.form['nombre']
    localization= request.form['localizacion']
    favorites = 0
    date_ = datetime.now()

   
    if name == '' or localization == '':
        flash('Debes llenar todos los campos')
        return redirect(url_for('appPage.home'))
        

        
    project = Projects.query.filter_by(name=name).first()
   
    if project: 
        flash('Proyecto existente, cambia de nombre')
        return redirect(url_for('appPage.home'))
    
    newProject = Projects( name=name, localization=localization,favorites=favorites, date_=date_)
    db.session.add(newProject)
    db.session.commit()
    return redirect(url_for('appPage.home'))