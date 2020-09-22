from flask import Flask, request, render_template
import functions.f
import os


project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')
app = Flask(__name__, template_folder=template_path)


@app.route('/')
def index():
    return render_template('templates/index.html')


@app.route('/lliga')
def lliga():
    return render_template('templates/lliga.html')


@app.route('/lliga', methods=['POST'])
def formulari_post():
    # processem les dades del formulari
    nom = request.form["nom"]

    return "Salut, {}".format(nom)

# arranquem l'aplicació
app.run(debug=True)
