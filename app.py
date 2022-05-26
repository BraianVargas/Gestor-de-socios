from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

app.config.from_pyfile("src/data/config.py")


from src.classes.models import personClass, payClass, debtsClass, socioClass, familyClass, db



@app.route('/')
def index():
    return 'API REST 25'
@app.route('/nuevo/socio', methods=['POST', 'GET'])
def nuevo_socio():
    new_socio = None
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        age = request.form['age']
        address = request.form['address']
        dni = request.form['dni']
        phone = request.form['phone']
        email = request.form['email'] # Hasta aqui lo de persona
        wayToPay = request.form['wayToPay']
        permission = request.form['permission']
        # family = request.form['family']
        family = None
        withDebt = request.form['withDebt']
        debt = request.form['debt']
        typeSocio = request.form['typeSocio']
        new_socio = socioClass(name, lastname, age, address, dni, phone, email, wayToPay, permission, family, withDebt, debt, typeSocio)
        db.session.add(new_socio)
        db.session.commit()
        return jsonify(new_socio)
    else:
        return render_template('nuevo_socio.html', json = jsonify(new_socio))


if __name__ == '__main__':
        app.run(debug=True)
    