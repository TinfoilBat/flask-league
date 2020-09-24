from flask import Flask, request, render_template
import functions.f as f
import functions.globals as g
import os


project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')
app = Flask(__name__, template_folder=template_path)

g.teams = f.create_teams("teams.cfg")
g.league = f.create_league(g.teams)
g.ranking = f.create_ranking(g.teams)

@app.route('/')
def index():
    return render_template('templates/index.html')


@app.route('/lliga')
def lliga():
    return render_template('templates/lliga.html', teams=g.teams, league=g.league)


@app.route('/lliga', methods=['POST'])
def formulari_lliga_post():
    # processem les dades del formulari
    loc = request.form["local"]
    loc_goals = request.form["local_number"]
    visit = request.form["visiting"]
    visit_goals = request.form["visiting_number"]
    f.update_league(loc, loc_goals, visit, visit_goals)
    f.calculate_ranking(loc, loc_goals, visit, visit_goals)

    return render_template('templates/lliga.html', teams=g.teams, league=g.league)

@app.route('/ranking')
def ranking():
  return render_template('templates/ranking.html', teams=g.teams, league=g.league)

@app.route('/ranking', methods=['POST'])
def ranking_post():
  pass

# arranquem l'aplicació
if __name__ == "__main__":
  app.run(debug=True)
