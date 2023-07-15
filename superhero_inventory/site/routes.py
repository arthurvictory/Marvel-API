from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from superhero_inventory.forms import SuperheroForm
from superhero_inventory.models import Superhero, db

site = Blueprint('site', __name__, template_folder = 'site_templates')


@site.route('/')
def home():
    print('look at this cool project. Would you just look at it')
    return render_template('index.html')

@site.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    superheroform = SuperheroForm()

    try:
        if request.method == 'POST' and superheroform.validate_on_submit():
            name = superheroform.name.data
            description = superheroform.description.data
            price = superheroform.price.data 
            quality = superheroform.quality.data
            user_token = current_user.token

            superhero = Superhero(name, description, price, quality, user_token)

            db.session.add(superhero)
            db.session.commit()

            return redirect(url_for('site.profile'))
    
    except:
        raise Exception('Superhero not created, check your info and try again!')

    user_token = current_user.token
    superheroes = Superhero.query.filter_by(user_token = user_token)


    return render_template('profile.html', form = superheroform, superheroes = superheroes)