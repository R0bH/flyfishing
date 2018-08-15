from flask import Flask, render_template, request
# Import the fixer
from werkzeug.contrib.fixers import ProxyFix

from forms import ContactForm

#from access_api import get_games_won

app = Flask(__name__)
app.secret_key = 'superSecret'
app.wsgi_app = ProxyFix(app.wsgi_app)

summoner_name = 'uberwold'
@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    #if request.method == 'GET':
    #    summoner_name = 'uberwold'
    #    value = [summoner_name,get_games_won(summoner_name)]
    return render_template('index.html',value='test', form=form)
    #if request.method == 'POST':
    #    summoner_name=str(form.name.data)
    #    value = [summoner_name,get_games_won(summoner_name)]
    #    return render_template('stats.html',summoner_name=summoner_name,value=value)

@app.route('/about')
def about():
    return render_template('about.html' )

@app.route('/stats')
def stats():
    form = ContactForm()
    return render_template('stats.html', form=form )

if __name__ == '__main__':
  app.run(debug=True)
