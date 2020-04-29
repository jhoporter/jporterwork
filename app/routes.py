from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import ContactForm
import os
import smtplib, ssl




@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


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
        recipient = "jmporterwork@gmail.com"
        server.starttls()
        server.login("jmporterwork@gmail.com", "cy(5U((jj,r@RPMr%(CZ")
        server.sendmail("jmporter@gmail.com", recipient, send)
        flash('Message sent!')
        return redirect(url_for('contact'))
    return render_template('contact.html', title='Contact', form=form)
