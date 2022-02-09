# package imports
from flask import Blueprint, flash, render_template, request, redirect, url_for

# project file imports
from drone_inventory.forms import UserLoginForm

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email,password)

            flash(f'You have successfully created a user account for {email}', 'user-created')
            return redirect(url_for('auth.signin'))

    except:
        raise Exception('Invalid Form Data: Please check your form')

    return render_template('signup.html', form=form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    return render_template('signin.html', form=form)