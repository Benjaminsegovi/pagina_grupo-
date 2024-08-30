from flask import Flask, render_template # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente

def box1():

   return render_template('inicio.html') 

@app.route('/Entradas')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente

def box2():

   return render_template('entradas.html')

@app.route('/Fondos')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente

def box3():

   return render_template('fondos.html')

@app.route('/Postres')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente

def box4():

   return render_template('postres.html')

@app.route('/Vinos')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente

def box5():

   return render_template('vinos.html')

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente   

   app.run(debug=True)