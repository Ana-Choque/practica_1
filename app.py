from flask import Flask,render_template,request

app =  Flask (__name__)

# Página de inicio
@app.route('/')
def index():
    return render_template('inicio.html')

# Página "Quiénes somos"
@app.route('/quienes_somos')
def about():
    return render_template('quienes_somos.html')

# Página de servicios
@app.route('/servicios')
def services():
    return render_template('servicios.html')

# Página de noticias
@app.route('/noticias')
def news():
    return render_template('noticias.html')

# Página de contacto
@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Aquí puedes gestionar los datos del formulario
        return render_template('thankyou.html', name=name)
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)