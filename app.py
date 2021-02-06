from flask import *
from models import *
import os
app=Flask(__name__)
app.secret_key=os.urandom(24)
loggedIn=None 
app.config["SQLALCHEMY_DATABASE_URI"]=mydb
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["DEBUG"]=True
db.init_app(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login1',methods=['POST'])
def login1():
    n=request.form.get('username')
    p=request.form.get('password')
    users=User.query.all()
    try:
        for u in users:
          if u.email==n and u.password == p:
            global loggedIn
            loggedIn=u
            return redirect(url_for('dashboard'))
        else:
            return redirect (url_for('login'))
    except KeyError:
        return "No such User Exist"
    except Exception as e:
        return str(e)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/r1',methods=["POST"])
def r1():
    name=request.form.get('name')
    #username=request.form.get('username')
    email=request.form.get('email')
    number=request.form.get('no')
    password=request.form.get('repassword')
    user=User(name=name,email=email,number=number, password=password)
    db.session.add(user)
    db.session.commit()
    return render_template('registered.html',name=name,email=email,no=number)
    
@app.route("/dashboard")
def dashboard():
    global loggedIn
    if loggedIn:
        return render_template("dashboard.html",user=loggedIn)
    else:
        return redirect(url_for('login'))
    

@app.route('/friendlist')
def friendlist():
    global loggedIn
    userId=loggedIn.id      #id is user id
    friendlist=MakeFriend.query.filter_by(userid=userId).all()
    friends=[]
    for f in friendlist:
        friends.append(User.query.filter_by(id=f.friendid).first())
    return render_template("friendlist.html",friends=friends, users=User.query.all())

@app.route('/addf1',methods=["POST"])
def addf1():
    global loggedIn
    username=request.form.get('username')
    #return render_template("error.html", t=username)
    f=User.query.filter_by(email=username).first()
    mk=MakeFriend(userid=loggedIn.id, friendid=f.id)
    db.session.add(mk)
    mk=MakeFriend(userid=f.id, friendid=loggedIn.id)
    db.session.add(mk)
    db.session.commit()
    
    return redirect(url_for('friendlist'))

@app.route('/logout')
def logout():
    global loggedIn
    loggedIn = None
    return redirect(url_for('login'))
@app.route('/<int:id>')
def profile(id):
    #Show the profile of that user 
    user=User.query.get(id)
    return render_template("profile.html",user=user)



app.run()