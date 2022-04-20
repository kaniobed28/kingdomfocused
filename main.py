from email import message
from argon2 import hash_password
from flask import Flask,redirect,url_for,render_template,request
import flask_login
from flask_sqlalchemy import SQLAlchemy
#Make sure that flask_login and bcrypt are installed
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1.db'
db = SQLAlchemy(app)
app.secret_key = "this is my secrete key"
class Registed_Person(db.Model,):
    """Model for user accounts."""
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True)
    fname = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    lname = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    mname = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    age = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    pnumber = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    gnumber = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    gender = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    htown = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    raddress = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    bdate = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    nationality = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    password = db.Column(db.String(50),
                         nullable=False,
                         unique=False)
    
    
    def __repr__(self):
        return '<User {}>'.format(self.fname)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
       
        return render_template('index.html')
    return render_template('index.html')


@app.route('/complete',methods=['POST'])
def complete():
    if request.method=='POST':
        # Handle POST Request here
        fname = request.form['fname']
        lname = request.form['lname']
        mname = request.form['mname']
        pnumber = request.form['pnumber']
        gnumber = request.form['gnumber']
        age = request.form['age']
        email = request.form['email']
        htown = request.form['htown']
        raddress = request.form['raddress']
        bdate = request.form['bdate']
        gender = request.form['gender']
        nationality = request.form['nationality']
        password = request.form['password']
        hash_pwd = generate_password_hash(password)
        newly_registered_person = Registed_Person(fname = fname,lname = lname,mname= mname,pnumber = pnumber,nationality= nationality,
        gnumber= gnumber,age = age,email = email,htown =htown,raddress =raddress,
        bdate = bdate,gender= gender,password = str(hash_pwd))
        check_register = Registed_Person.query.filter_by(email = email).first()
        if check_register:
            return render_template('complete.html',message = "Please your email already exist in our database.")
        else:

            db.session.add(newly_registered_person)
            db.session.commit()

            return render_template('complete.html',message = f'You are welcome {fname} {lname}')
@app.route("/register_people")
def register_people():
    all_members = Registed_Person.query.all()
    return render_template('register_people.html',all_members = all_members)
db.create_all()
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)