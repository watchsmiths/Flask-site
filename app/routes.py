from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
import requests, os
from PIL import Image

from app import app, db, bcrypt, forms
from .forms import Sellwatch, Contact, newsletter
# from .models import User 


@app.route('/', methods=["GET", "POST"])
def home():
    newsletter_form = newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
    
    return render_template('index.html', newsletter_form=newsletter_form)

@app.route('/about', methods=['GET','POST'])
def about():
    newsletter_form=newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
    
    return render_template('about.html', title = 'About Us', newsletter_form=newsletter_form)

@app.route('/brands', methods=['GET','POST'])
def brands():
    brands = [
        {
            'name': 'Audemars Piguet',
            'image': 'AP.jpg'
        },
        {
            'name': 'Breitling',
            'image': 'breitling.jpg'
        },
        {
            'name': 'Hublot',
            'image': 'hublot.jpg'
        },
        {
            'name': 'Omega',
            'image': 'omega.jpg'
        },
        {
            'name': 'Patek Philippe',
            'image': 'patek.jpg'
        },
        {
            'name': 'Piaget',
            'image': 'piaget.jpg'
        },
        {
            'name': 'Rolex',
            'image': 'rolex.jpg'
        },
        {
            'name': 'Sale',
            'image': 'sale.jpg'
        },
    ]
    newsletter_form= newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
    
    return render_template('watch_brands.html', title='Brands', brandnames=brands, newsletter_form=newsletter_form)

@app.route('/brands/<watch_brand>', methods=['GET','POST'])
def watchbrand(watch_brand):
    newsletter_form = newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
    
    watches = [
        {
            'Brand': '',
            'name': '',
            'price': '',
            'discount': '',
            'image_1': '',
            'image_2': '',
            'image_3': '',
            'image_4': ''
        },
        {
            'Brand': '',
            'name': '',
            'price': '',
            'discount': '',
            'image_1': '',
            'image_2': '',
            'image_3': '',
            'image_4': ''
        },
        {
            'Brand': '',
            'name': '',
            'price': '',
            'discount': '',
            'image_1': '',
            'image_2': '',
            'image_3': '',
            'image_4': ''
        },
        {
            'Brand': '',
            'name': '',
            'price': '',
            'discount': '',
            'image_1': '',
            'image_2': '',
            'image_3': '',
            'image_4': ''
        },
        {
            'Brand': '',
            'name': '',
            'price': '',
            'discount': '',
            'image_1': '',
            'image_2': '',
            'image_3': '',
            'image_4': ''
        },
        {
            'Brand': '',
            'name': '',
            'price': '',
            'discount': '',
            'image_1': '',
            'image_2': '',
            'image_3': '',
            'image_4': ''
        },
        {
            'Brand': '',
            'name': '',
            'price': '',
            'discount': '',
            'image_1': '',
            'image_2': '',
            'image_3': '',
            'image_4': ''
        },
        {
            'Brand': '',
            'name': '',
            'price': '',
            'discount': '',
            'image_1': '',
            'image_2': '',
            'image_3': '',
            'image_4': ''
        },
    ]

    if watch_brand not in brands():
        abort(404)
    else:
        return render_template('brandpage.html', watch_brand=watch_brand, newsletter_form=newsletter_form)
   
@app.route('/product', methods=['GET','POST'])
def product():
    newsletter_form = newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
    
    return render_template('product.html', title='Product', newsletter_form=newsletter_form)

@app.route('/sale', methods=['GET','POST'])
def sale():
    newsletter_form = newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
    
    return render_template('sale.html', title = 'Sale', newsletter_form=newsletter_form)

@app.route('/sell_watch', methods=['GET', 'POST'])
def sellwatch():
    form = Sellwatch() 
    newsletter_form=newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
    
    return render_template('sell_watch.html', title = 'Sell Your Watch', form=form, newsletter_form=newsletter_form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Contact()
    newsletter_form=newsletter()
    
    if form.validate_on_submit():
        flash(f'Thank you for your enquiry, confirmation of recipt will be sent to {form.email.data}. We aim to get back to you shortly', "success")
        return redirect(url_for('home'))
    return render_template('contact.html', title = 'Contact Us', form=form, newsletter_form=newsletter_form)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    newsletter_form=newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
    
    return render_template('cart.html', title='Cart', newsletter_form=newsletter_form)

@app.errorhandler(404)
def not_found_error(error):
    newsletter_form=newsletter()
    return render_template('404.html', newsletter_form=newsletter_form), 404


# @app.route('/account')
# def account():
#     if 'email' not in session:
#         flash(f'Please login first', 'danger')
#         return redirect(url_for('login'))
#     return render_template('admin/index.html', title='Account Page')



# @app.route('/admin/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm(request.form)
#     if request.method == 'POST' and form.validate():
#         hash_password = bcrypt.generate_password_hash(form.password.data)
        
#         user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data,
#                     password=hash_password)
#         db.session.add(user)
#         db.session.commit()
#         flash(f'Welcome {form.firstname.data}, Thank you for registering','success')
#         return redirect(url_for('account'))
#     return render_template('admin/register.html', form=form, title="Register User")


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm(request.form)
#     if request.method == "POST" and form.validate():
#         user = User.query.filter_by(email = form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data): 
#             session['email'] = form.email.data
#             flash(f'Welcome {User.firstname}, You are now logged in', 'success')
#             return redirect(request.args.get('next') or url_for('account'))
#         else:
#             flash('Wrong Password, please try again', 'danger')
#     return render_template('admin/login.html', form=form, title="login")
