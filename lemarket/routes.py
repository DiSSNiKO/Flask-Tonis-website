from sqlalchemy import true
from lemarket import webapp
from lemarket.forms import LoginForm, RegisterForm
from flask import render_template, redirect, url_for, flash
from lemarket import db
from lemarket.models import itemData, User
def isInDbase(newname):
        user = User.query.filter_by(username=newname).first()
        if user!=None:
            return True
        return False
@webapp.route("/")
@webapp.route("/home") 
def home_page():
    return render_template('home.html')

@webapp.route("/market")
def market():
    item = itemData.query.all()
    return render_template('market.html', items=item)
@webapp.route("/register", methods=["GET","POST"])
def register_page():
    form = RegisterForm()
    registerfail = False
    if form.validate_on_submit():
        print(f"wtf is this {isInDbase(form.username.data)}")
        if isInDbase(form.username.data)==False:
            user_to_add = User(username=form.username.data, email= form.email.data, password_hash = form.password1.data)
            db.session.add(user_to_add)
            db.session.commit()
            return redirect(url_for('home_page'))
        else:
            registerfail = true
    if form.errors!={}:
        registerfail = true
    return render_template('register.html', usableForm = form, registerfailed=registerfail)
@webapp.route("/login", methods=["GET","POST"])
def logeen():
    form = LoginForm()
    uname = form.username.data
    upass = form.password.data 
    usercheck = User.query.filter_by(username=uname).first()
    loginfail = False
    if usercheck!=None and usercheck.password_hash==upass:
        loggedinuser = User(username=usercheck.username, password_hash=usercheck.password_hash, email=usercheck.email, budget=usercheck.budget)
        return render_template('/welcome.html', loggedinuser=loggedinuser)
    elif uname!=None and upass!=None:
        loginfail=True
        print(uname, upass)
    return render_template('/login.html', loginform = form, loginfail=loginfail)
if __name__ == "__main__":
    webapp.run(debug=True)
