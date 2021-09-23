from flask import Flask, url_for, render_template, redirect, request
from app import app, db
from app.model.tables import User
import requests


@app.route("/", methods=['GET', 'POST'])
def index():
    allUsers = User.query.all()

    if (request.method == 'POST'):
        newUser = User(request.form['name'],
                       request.form['age'],
                       request.form['email'],
                       request.form['phone'])

        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('index', users = allUsers))

    return render_template('index.html', users = allUsers)


@app.route("/create")
def create():
    return render_template('create.html')


@app.route("/delete/<id>", methods=['GET'])
def delete(id):
    allUsers = User.query.all()
    userToDelete = User.query.get(id)
    db.session.delete(userToDelete)
    db.session.commit()
    return redirect(url_for('index', users = allUsers))
