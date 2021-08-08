import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import (
    Flask, render_template, request,
)
from werkzeug.security import generate_password_hash, check_password_hash
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}".format(
    user=os.getenv("POSTGRES_USER"),
    passwd=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=5432,
    table=os.getenv("POSTGRES_DB")
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
print(os.getenv("POSTGRES_USER"))

class UserModel(db.Model):
    __tablename__="users"

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=("GET", "POST"))
def register(): 
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        if not username: 
            error = "Username is required."
        elif not password: 
            error = "Password is required."
        elif UserModel.query.filter_by(username=username).first() is not None: 
            error = f"User {username} is already registered."
        
        if error is None: 
            new_user = UserModel(username, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return f"User {username} created successfully"
        else: 
            return error, 418

    return render_template("register.html")

@app.route('/login', methods=("GET", "POST"))
def login(): 
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None
        user = UserModel.query.filter_by(username=username).first()

        if user is None: 
            error = "Incorrect username"
        elif not check_password_hash(user.password, password): 
            error = "Incorrect password."
        
        if error is None: 
            return "Login Successful", 200
        else: 
            return error, 418

    return render_template("login.html")

@app.route('/flights')
def flights():
    return render_template("flights.html")

@app.route('/flightsAPI', methods=("GET", "POST"))
def flightsAPI(): 
    if request.method=="POST":
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        departDate = request.form.get("departDate")
        returnDate = request.form.get("returnDate")
        error = None
    
    url = f'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/{origin}-sky/{destination}-sky/{departDate}'
    querystring = {"inboundpartialdate":returnDate}
    headers = {
        'x-rapidapi-key': os.getenv("SKYSCANNER_KEY"),
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
        

    return response.text