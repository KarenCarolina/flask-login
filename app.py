from flask import Flask,render_template,url_for,redirect,make_response,session
from flask_login import login_required,LoginManager,login_user,UserMixin,logout_user
from os import urandom
from forms import LoginForm, SignUpForm,ProjectForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/base.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)
app.config["SECRET_KEY"]=urandom(16)


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(30),unique=True)
    password=db.Column(db.String(30))
 
class Project(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  title=db.Column(db.String(30))
  description=db.Column(db.String(250))

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/",methods=["GET","POST"])
def index():
    projects=db.engine.execute("select * from project")
    context={
        "projects":projects
    }
    return(render_template("index.html",**context))


@app.route("/sign-up", methods=["GET","POST"])
def sign_up():
    sign_up_form=SignUpForm()
    context={
        "sign_up_form" : sign_up_form
    }
    if sign_up_form.validate_on_submit():
        email=sign_up_form.email.data
        password=sign_up_form.password.data
        user=User(email=email,password=password)
        if user is not None:
            db.session.add(user)
            db.session.commit()
            return redirect("/sign-up")
    return render_template("sign-up.html",**context)


@app.route("/login",methods=["GET","POST"])
def login():
    login_form = LoginForm()
    context = {
        "login_form": login_form
    }
    if login_form.validate_on_submit():
        email=login_form.email.data
        session["email"]=email
        password=login_form.password.data
        user=User.query.filter_by(email=email,password=password).first()
        if user is not None:
            login_user(user)
            return redirect("/welcome")
        else:
            return redirect("/login")
    return(render_template("login.html",**context))


@app.route("/welcome",methods=["GET","POST"])
@login_required
def welcome():
    project_form=ProjectForm()
    context={
        "project_form":project_form
    }
    if project_form.validate_on_submit():
        title=project_form.title.data
        description=project_form.description.data
        pro=Project(title=title,description=description)
        if(pro is not None):
            db.session.add(pro)
            db.session.commit()
            return(redirect("/welcome"))
    return(render_template("welcome.html",**context))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html",error=error)


@app.errorhandler(401)
def not_found(error):
    return render_template("error.html",error=error)


# if __name__ == "__main__":
#     app.run(debug=True)
