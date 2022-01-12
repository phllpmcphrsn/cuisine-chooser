from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cuisine.db'  # 3 slashes so that it'll reside in our pwd
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
        exists = Cuisine.query.filter_by(cuisine=cuisine_entry).first()
        if exists is not None:
            message = {'error': 'Generate or add a cuisine by pressing one of the buttons below'}
            return render_template('index.html', message=message)
        
        new_cuisine = Cuisine(cuisine=cuisine_entry)
        if 'add' in request.form:
            try:
                # commit to db, redirect to main page
                db.session.add(new_cuisine)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                return 'There was an issue adding your task', e
        elif 'generate' in request.form:
            # Choose cuisine from database
            chosen_cuisine = random.choice(Cuisine.query.all())
            return render_template('index.html', message=chosen_cuisine)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    # setting debug to True to show any errors
    # on web page
    app.run(debug=True)
