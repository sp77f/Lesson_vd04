from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/contacts/')
def about():
    return render_template("contacts.html")

@app.route('/prepod/')
def prepod():
    return render_template("prepod.html")

if __name__ == '__main__':
    app.run()