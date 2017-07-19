from flask import Flask, jsonify, render_template, request, session, redirect, url_for, make_response
from forms import GetuserForm, GetdomainForm, GetallForm, PutuservexForm, PutdomainvexForm
from apiTool import user_get, domain_get, mbx_get, user_vex, domain_vex, mbx_get_list
import json
from flask_mail import *
import pprint

app = Flask(__name__)
mail = Mail(app)

app.secret_key = "development-key"


# Index view
@app.route("/")
def index():
    return render_template("index.html")

# GET user info view
@app.route("/get/user", methods=['GET', 'POST'] )
def getuser():
    form = GetuserForm()

    if request.method == 'POST':
        success = 'Task complete!'
        method = 'GET'
        cst_id = request.form['customer_id']
        domain = request.form['domain']
        user = request.form['user']
        mbx_type = request.form['mbx_type']
        data = user_get(cst_id, domain, mbx_type, user)
        return render_template("getuser.html", data=data,
                                cst_id=cst_id, domain=domain,
                                user=user, mbx_type=mbx_type,
                                method=method, form=form,
                                success=success)
    elif request.method == "GET":
        return render_template("getuser.html", form=form)

# GET domain info
@app.route("/get/domain", methods=['GET', 'POST'] )
def getdomain():
    form = GetdomainForm()

    if request.method == 'POST':
        success = 'Task complete!'
        method = 'GET'
        cst_id = request.form['customer_id']
        domain = request.form['domain']
        mbx_type = request.form['mbx_type']
        data = domain_get(cst_id, domain, mbx_type)
        return render_template("getdomain.html", data=data,
                                cst_id=cst_id, domain=domain,
                                mbx_type=mbx_type, method=method,
                                form=form, success=success)
    elif request.method == "GET":
        return render_template("getdomain.html", form=form)

# GET all users from a domain
@app.route("/get/all", methods=['GET', 'POST'] )
def getall():
    form = GetallForm()

    if request.method == 'POST':
        success = 'Task complete!'
        method = 'GET'
        cst_id = request.form['customer_id']
        domain = request.form['domain']
        mbx_type = request.form['mbx_type']
        data = mbx_get_list(cst_id, domain, mbx_type)
        return render_template("getall.html", data=data,
                                cst_id=cst_id, domain=domain,
                                mbx_type=mbx_type, method=method,
                                succes=success, form=form)
    elif request.method == "GET":
        return render_template("getall.html", form=form)

# PUT true/false value on User
@app.route("/put/uservex", methods=['GET', 'POST'] )
def put_uservex():
    form = PutuservexForm()

    if request.method == 'POST':
        success = 'Task complete!'
        method = 'PUT'
        cst_id = request.form['customer_id']
        domain = request.form['domain']
        mbx_type = request.form['mbx_type']
        user = request.form['user']
        user_vex_val = request.form['user_vex_val']
        data = user_vex(cst_id, domain, mbx_type, user, user_vex_val)
        return render_template("uservex.html", form=form,
                                cst_id=cst_id, domain=domain,
                                mbx_type=mbx_type, user=user,
                                user_vex_val=user_vex_val,
                                data=data, success=success)
    elif request.method == "GET":
        return render_template("uservex.html", form=form)

# PUT true/false value on entire domain
@app.route("/put/domainvex", methods=['GET', 'POST'] )
def put_domainvex():
    form = PutdomainvexForm()

    if request.method == 'POST':
        success = 'Task complete!'
        cst_id = request.form['customer_id']
        domain = request.form['domain']
        mbx_type = request.form['mbx_type']
        domain_vex_val = request.form['domain_vex_val']
        data = domain_vex(cst_id, domain, mbx_type, domain_vex_val)
        return render_template("domainvex.html", form=form,
                                cst_id=cst_id, domain=domain,
                                mbx_type=mbx_type, user=user,
                                domain_vex_val=domain_vex_val,
                                data=data, success=success)
    elif request.method == "GET":
        return render_template("domainvex.html", form=form)

# Feedback Form view
@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # From User
        name = request.form['name']
        email = request.form['email']
        body = request.form['body']
        subject = "New Feedback from %s (%s)!" % (name, email)

        # Needs to updated to whatever user is relaying.
        sender = "ubuntu@ip-172-31-14-105.us-west-2.compute.internal"
        # Administrator contact list
        admins = ['rudy.marks@gmail.com']

        success = "Thanks! It worked!"

        msg = Message(subject, sender=sender, recipients=admins)
        msg.body = body
        mail.send(msg)

        return render_template("feedback.html", success=success)

    if request.method == 'GET':
        return render_template("feedback.html")

# Getting Started view

# Examples view

# Download Script view



if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)
