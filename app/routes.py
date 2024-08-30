from flask import render_template, request, redirect, url_for
from app import app

cards = []
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        #создаёт условие для проверки наличия данных в полях username, city , hobby age
        if username and city and hobby and age:
            cards.append({'username': username, 'city': city, 'hobby': hobby, 'age': age})
            return redirect(url_for('index'))
    return render_template('users.html', cards=cards)