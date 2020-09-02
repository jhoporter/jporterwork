from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import ContactForm
import os
import smtplib, ssl




@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        article_type = form.article_type.data
        word_count = form.word_count.data
        message = form.message.data
        subject = "Inquiry from " + name + "---" + email
        text = "Type:" + " " + article_type + " \n" + "Word count: " + word_count + " \n" + "Message: " + message
        send = 'Subject: {}\n\n{}'.format(subject, text)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        recipient = "jhoporter@gmail.com"
        sender = "jhoporter@gmail.com"
        server.starttls()
        server.login(sender, "Q1Hw4EJnXq2btp3q6Vfp")
        server.sendmail(sender, recipient, send)
        flash('Message sent!')
        return redirect("/index#contact")
    return render_template('index.html', title='Home', form=form)


@app.route('/samples')
def samples():
    return render_template('samples.html', title='Samples')


@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        article_type = form.article_type.data
        word_count = form.word_count.data
        message = form.message.data
        subject = "Inquiry from " + name + "---" + email
        text = "Type:" + " " + article_type + " \n" + "Word count: " + word_count + " \n" + "Message: " + message
        send = 'Subject: {}\n\n{}'.format(subject, text)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        recipient = "jhoporter@gmail.com"
        sender = "jhoporter@gmail.com"
        server.starttls()
        server.login(sender, "Q1Hw4EJnXq2btp3q6Vfp")
        server.sendmail(sender, recipient, send)
        flash('Message sent!')
        return redirect(url_for('contact'))
    return render_template('contact.html', title='Contact', form=form)



## BLOG ##
@app.route('/ordering-takeout-in-a-pandemic')
def ordering():
    return render_template('blog-ordering-takeout.html', title='Ordering Takeout in a Pandemic')



## SAMPLES ##
@app.route('/things-to-do-quarantine')
def tabletop():
    return render_template('sample-tabletop.html', title="Running Out Of Things To Do In Quarantine")


@app.route('/generate-passive-income')
def generatepassive():
    return render_template('sample-generate-passive-income.html', title="Generating Passive Income Through Continuity Marketing")

@app.route('/hiring-product-development-firm')
def hiringproduct():
    return render_template('sample-hiring-product-development.html', title='Hiring A Product Development Firm')


@app.route('/maximizing-the-effects-of-caffeine')
def coffee():
    return render_template('sample-maximizing-the-effects.html', title="Maximizing the Effects of Caffeine")


@app.route('/productivity-hacks')
def productivity():
    return render_template('sample-productivity-hacks.html', title="Productivity Hacks")


@app.route('/yamaha-hs7-review')
def yamaha():
    return render_template('sample-yamaha-hs7-review.html', title="Yamaha HS7 Review")


@app.route('/parcel-pending-press-release')
def parcel():
    return render_template('sample-parcel-pending.html', title="Parcel Pending Press Release")

@app.route('/wean-your-baby-with-fruits-and-vegetables')
def wean():
    return  render_template('sample-wean-your-baby.html', title="Wean Your Baby with Fruits and Vegetables")
