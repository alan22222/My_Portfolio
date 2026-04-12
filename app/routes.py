from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import ContactForm
from flask_mail import Message
from . import mail

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template('about.html')

@main.route("/about")
def about():
    return render_template('about.html')

@main.route("/projects")
def projects():
    return render_template('projects.html')

@main.route("/skills")
def skills():
    return render_template('skills.html')

@main.route("/experience")
def experience():
    return render_template('experience.html')

@main.route("/education")
def education():
    return render_template('education.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        try:
            msg = Message(
                subject="Contact Form Message",
                sender='alanchacko42@gmail.com',
                recipients=['alanchacko42@gmail.com'],
                reply_to=form.email.data
            )
            msg.body = f"""
From: {form.name.data} <{form.email.data}>

{form.message.data}
"""
            mail.send(msg)
            flash("Message sent successfully!")
            return redirect(url_for('main.contact'))
        except Exception as e:
            return f"Mail failed: {e}"

    if request.method == 'POST':
        flash(str(form.errors))

    return render_template('contact.html', form=form)