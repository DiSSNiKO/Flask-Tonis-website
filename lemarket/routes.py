from lemarket import webapp
from lemarket.forms import RegisterForm
from flask import render_template
from lemarket.models import itemData
@webapp.route("/")
@webapp.route("/home") 
def home_page():
    return render_template('home.html')

@webapp.route("/market")
def market():
    item = itemData.query.all()
    return render_template('market.html', items=item)
@webapp.route("/register")
def register_page():
    form = RegisterForm()
    return render_template('register.html', usableForm = form)
if __name__ == "__main__":
    webapp.run(debug=True)
