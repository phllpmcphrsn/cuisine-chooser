from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import random 
import os

app = Flask(__name__)
# grab FLASK_APP_SETTINGS; otherwise use DevConfig
env_config = os.getenv("FLASK_APP_SETTINGS", "config.DevelopmentConfig") 
app.config.from_object(env_config)
db = SQLAlchemy(app)


class Cuisine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuisine = db.Column(db.String(50), unique=True, nullable=False)
            
    def __repr__(self):
        return '<Cuisine %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cuisine_entry = str.title(request.form['cuisine'])
        if not cuisine_entry:
            return redirect('/')
        
        new_cuisine = Cuisine(cuisine=cuisine_entry)
        if 'add' in request.form and new_cuisine is not None:
            try:
                # commit to db, redirect to main page
                db.session.add(new_cuisine)
                db.session.commit()
            except Exception as e:
                return 'There was an issue adding your task', e
            else:
                return render_template('index.html')
        elif 'generate' in request.form:
            # Choose cuisine from database
            chosen_cuisine = random.choice(Cuisine.query.all())
            return render_template('index.html', message=chosen_cuisine)
    else:
        # GET
        # Grab the first cuisine so that we have something to display
        # upon loading the webpage 
        default_cuisine = Cuisine.query.get(1)
        return render_template('index.html', message=default_cuisine)


if __name__ == "__main__":
    # setting debug to True to show any errors
    # on web page
    app.run(debug=False)
