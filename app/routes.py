from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
from app.Alphademo import Alphademo

print('routes importing done')

#car=Alphademo()

@app.route('/')
@app.route('/index')
def index():
    user  = { 'username':'steven'}
    posts = [
        {
            'author':{'username': ' John'},
            'body': 'Beautiful day in Edmonton'
        },
        {   'author':{'username': 'Sue'},
            'body': 'Wonderful day in the neighborhood'
        }
    ]
    return render_template('index.html',title='OOO', user=user, posts=posts )

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        #renderval = render_template('login.html', title='Sign In', form=form)
        return redirect('/index')
#       flash('Form data failed validation. user {}, password {}'.format(
#            form.username.data, form.password.data))
    renderval = render_template('login.html', title='Sign In', form=form)
    # login view function goes all the way though and gets rendered here below
    return renderval



