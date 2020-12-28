from flask import Flask, render_template,request,redirect
from datetime import datetime

# para trabajar con formularios
from flask_wtf import FlaskForm
from wtforms import StringField ,TextAreaField
from wtforms.validators import DataRequired,Email
from wtforms.fields.html5 import EmailField
app = Flask(__name__)
app.config.from_pyfile('config.cfg')

class Formulario(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    text = TextAreaField('text',validators=[DataRequired()])
    mail = EmailField('mail',validators=[DataRequired()])


class Persona():
    def __init__(self,nombre,apellido,nac):
        self.nombre = nombre
        self.apellido = apellido
        self.nac = nac
    
    def edad(self):
        return self.__fecha().year - self.nac
 
    def __fecha(self):
        fecha = datetime.now()
        return fecha

class Estudiante(Persona):

    def __init__(self,nombre,apellido,nac,carrera,id_estudiante):
        self.carrera = carrera
        self.id_estudiante = id_estudiante
        Persona.__init__(self,nombre,apellido,nac)


mario = Persona('Mario','Perez',1960)
julia = Estudiante('Julia','Lopez',2000,'Ing. Sistemas',12087)

print(isinstance(mario,Estudiante))
print(isinstance(julia,Estudiante))



@app.route('/',methods=['POST','GET'])
def index():
    mario = Persona('Mario','Perez',1960)
    mario.apellido = 'Gonzales'
    julia = Estudiante('Julia','Lopez',2000,'Ing. Sistemas',12087) 
    form = Formulario()
    if request.method == 'POST':
        data = request.form
        return data

   
   
    return render_template('index.html',mario=mario,julia=julia,form=form)



if __name__ == "__main__":
    app.run(debug=True)

