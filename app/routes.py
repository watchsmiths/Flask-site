from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
import requests, os, sqlite3

from app import app, db, forms, mail
# from app import bcrypt
from .forms import Sellwatch, Contact, newsletter
from .models import Brands, Products 
from flask_mail import Message

conn = sqlite3.connect('myshop.db')




@app.route('/', methods=["GET", "POST"])
def home():
    newsletter_form = newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
        return (render_template('index.html', newsletter_form=newsletter_form))
    


    return render_template('index.html', newsletter_form=newsletter_form)

@app.route('/about', methods=['GET','POST'])
def about():
    newsletter_form=newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
        return (render_template('about.html', title = 'About Us', newsletter_form=newsletter_form))
    
    return render_template('about.html', title = 'About Us', newsletter_form=newsletter_form)

@app.route('/brands/', methods=['GET','POST'])
def brands():
    
    newsletter_form= newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
        return (render_template('watch_brands.html', title = 'Brands', newsletter_form=newsletter_form))
    
    return render_template('watch_brands.html', title='Brands', brandnames=Brands.query.all(), newsletter_form=newsletter_form)

@app.route('/brands/<string:watch_brand>/', methods=['GET','POST'])
def watchbrand(watch_brand):
    newsletter_form = newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
        return (render_template('brandpage.html', title=watch_brand, newsletter_form=newsletter_form))
    
    page = Brands.query.filter(Brands.name==watch_brand).all()
    watches = Products.query.filter_by(brand_name=watch_brand)
    

    if not page:
        abort(404)
    
    if page[0].name == 'Rolex' or page[0].name == 'Sale':
        return render_template('brandpage.html', title=watch_brand, watch_brand=watch_brand, watches=watches, newsletter_form=newsletter_form)
    else:
        return render_template('comingsoon.html', title=watch_brand, watch_brand=watch_brand, newsletter_form=newsletter_form)
   

@app.route('/brands/<string:watch_brand>/<int:watch_id>', methods=['GET','POST'])
def product(watch_brand, watch_id):
    newsletter_form = newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
        return (render_template('product.html', title=str(watch_brand+" "+watch.thumb_name), watch=watch, watch_brand=watch_brand, newsletter_form=newsletter_form))
    
    watch = Products.query.filter_by(brand_name=watch_brand, product_id=watch_id).first()
    watches = Products.query.filter(Products.product_id==watch_id).all()

    # thumbs = []
    # large = []

    # for filename in os.listdir(os.path.join(f'/images/products/watch/{ watch_brand }/{ watch.product_id }/')):
    #     if filename.startswith("PT"):
    #         thumbs.append(os.path.join(f'/images/products/watch/{ watch_brand }/{ watch.product_id }/', filename))
    #     elif filename.startswith("PL"):
    #         large.append(os.path.join(f'/images/products/watch/{ watch_brand }/{ watch.product_id }/', filename))
    #     else:
    #         continue


    if not watch:
        abort(404)

    if watches:
        return render_template('product.html', title=str(watch_brand+" "+watch.thumb_name), watch=watch, watch_brand=watch_brand, newsletter_form=newsletter_form)
        #  thumbs=thumbs, large=large)
    else:
        abort(404)



@app.route('/sale', methods=['GET','POST'])
def sale():
    newsletter_form = newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
        return (render_template('sale.html', title = 'Sale', newsletter_form=newsletter_form))
    
    return render_template('sale.html', title = 'Sale', newsletter_form=newsletter_form)

@app.route('/sell_watch', methods=['GET', 'POST'])
def sellwatch():
    form = Sellwatch() 
    newsletter_form=newsletter()
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
        return (render_template('sell_watch.html', title = 'Sell Your Watch', form=form, newsletter_form=newsletter_form))
    
    return render_template('sell_watch.html', title = 'Sell Your Watch', form=form, newsletter_form=newsletter_form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Contact()
    newsletter_form=newsletter()  
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
        return (render_template('contact.html', title = 'Contact Us', form=form, newsletter_form=newsletter_form))
    
    if request.method == "POST":
        email = form.email.data
        subject = form.subject.data
        message = form.description.data
        name = form.yourname.data

        msg = Message(subject=subject, body=message, sender=app.config['MAIL_USERNAME'], recipients=['enquiries@watchsmiths.co.uk'], reply_to=email)
        mail.send(msg)

        flash(f'Thank you for your enquiry, confirmation of recipt will be sent to {email}. We aim to get back to you shortly', "success")
        return render_template('contact.html', title = 'Contact Us', form=form, newsletter_form=newsletter_form)

    return render_template('contact.html', title = 'Contact Us', form=form, newsletter_form=newsletter_form)

@app.route('/contact/<string:watch_brand>/<string:watch_name>', methods=['GET', 'POST'])
def contacter(watch_brand, watch_name):   
    form = Contact()
    newsletter_form=newsletter()  
    if newsletter_form.validate_on_submit():
        flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
        return (render_template('contact.html', title = 'Contact Us', form=form, newsletter_form=newsletter_form, watch_name=watch_name, watch_brand=watch_brand))
    

    form.subject.data = f'Enquiry: {watch_brand} {watch_name}'

    if request.method == "POST":
        email = form.email.data
        subject = form.subject.data
        message = form.description.data
        name = form.yourname.data

        msg = Message(subject=subject, body=message, sender=app.config['MAIL_USERNAME'], recipients=['enquiries@watchsmiths.co.uk'], reply_to=email)
        mail.send(msg)

        flash(f'Thank you for your enquiry, confirmation of recipt will be sent to {email}. We aim to get back to you shortly', "success")
        return render_template('contact.html', title = 'Contact Us', form=form, newsletter_form=newsletter_form, watch_name=watch_name, watch_brand=watch_brand)


    #url logic
    page = Brands.query.filter(Brands.name==watch_brand).all()
    watches = Products.query.filter_by(brand_name=watch_brand)
    
    if not page:
        abort(404)
    
    
    # fix logic for entering any string in URL
    return render_template('contact.html', title = 'Contact Us', form=form, newsletter_form=newsletter_form, watch_name=watch_name, watch_brand=watch_brand)

@app.errorhandler(404)
def not_found_error(error):
    newsletter_form=newsletter()
    return render_template('404.html', newsletter_form=newsletter_form), 404


# Because of 'Sale' in brands db, the url goes to the display page instead of the sale page
@app.route('/brands/Sale', methods=['GET','POST'])
def nopage():
    abort(404)

@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "{:,.2f}".format(value)

# @app.route('/cart', methods=['GET', 'POST'])
# def cart():
#     newsletter_form=newsletter()
#     if newsletter_form.validate_on_submit():
#         flash(f"You've Been Added to The Mailing List, Your Discount Code Will Be Sent to {newsletter_form.email.data}", 'success')
#         return (render_template('cart.html', title = 'Cart', newsletter_form=newsletter_form))
    
#     return render_template('cart.html', title='Cart', newsletter_form=newsletter_form)


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
