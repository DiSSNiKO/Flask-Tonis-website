from lemarket import webapp
from lemarket.forms import LoginForm, RegisterForm, postForm
from flask import render_template, redirect, url_for, flash
from lemarket import db
from lemarket.models import postData, User
def isInDbase(newname):
        user = User.query.filter_by(username=newname).first()
        if user!=None:
            return True
        return False
@webapp.route("/")
@webapp.route("/home") 
def home_page():
    return render_template('home.html')


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
            registerfail = True
    if form.errors!={}:
        registerfail = True
    return render_template('register.html', usableForm = form, registerfailed=registerfail)
@webapp.route("/login", methods=["GET","POST"])
def logeen():
    form = LoginForm() 
    uname = form.username.data
    upass = form.password.data
    usercheck = User.query.filter_by(username=uname).first()
    loginfail = False
    
    if usercheck!=None and usercheck.password_hash==upass:
        
        return redirect(url_for('welcome_page', user=usercheck.id))
    
    elif uname!=None and upass!=None:
        loginfail=True
        print(uname, upass)
    return render_template('/login.html', loginform = form, loginfail=loginfail)



@webapp.route("/welcome/<user>", methods=["GET","POST"])
def welcome_page(user):
    currentuser = User.query.filter_by(id=user).first()
    newpostform = postForm()
    newpostformtext = newpostform.content.data
    userposts = postData.query.filter_by(owner=currentuser.id)
    if newpostformtext!=None:
        if newpostformtext != '' and len(newpostformtext)>2:
            print(newpostformtext)
            newpost = postData(content=newpostformtext, owner=currentuser.id)
            db.session.add(newpost)
            db.session.commit()
            newpostform.content.data = ''
            newpostformtext = newpostform.content.data
    return render_template("/welcome.html", currentuser=currentuser, postcontent=newpostform, userposts=userposts)



if __name__ == "__main__":
    webapp.run(debug=True)
