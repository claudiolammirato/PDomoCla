from flask import render_template, redirect, url_for, request
from flask.ext.login import login_required, login_user, logout_user
from ..models import User
from . import main
from .forms import LoginForm, ChangeUser
from ..ftparduino import ftparduino
from ..graph import graph


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data):
            return redirect(url_for('main.login', **request.args))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/temperature')
@login_required
def temperature():
    ftparduino()
    graph()
    return render_template('temperature.html')

@main.route('/impostazioni', methods=['GET', 'POST'])
@login_required
def impostazioni():
    form1 = ChangeUser()
    if form1.validate_on_submit():
        User.delete()
        User.register(form1.username.data, form1.password.data)
        return redirect(url_for('main.index'))
    return render_template('impostazioni.html', form1=form1)
