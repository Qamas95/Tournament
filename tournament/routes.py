from re import I
from tournament import app
from flask import render_template, redirect, url_for, flash
from tournament.models import Item, User
from tournament.forms import RegisterForm
from tournament import db


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/stats')
def stats():
    items = Item.query.all()
    return render_template('stats.html', items=items) 

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('stats'))
    if form.errors != {}: #if there is no errors from validations
        for err_msg in form.errors.values():
            flash(f'Error with creating user: {err_msg}')
    return render_template('register.html', form=form)

    
