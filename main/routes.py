from flask import Flask, request, make_response
from main import app, db
from main.database import Users
from flask_login import login_user, logout_user, login_required, current_user
from flask_cors import cross_origin

@app.route("/")
def index():
  return "TEsr"

@app.route("/get-user/<int:user_id>")
@cross_origin(origin='*')
@login_required
def getUser(user_id):
  try:
    curr_user = Users.query.where(Users.id == user_id).first()
    print(curr_user)
    return {
      "id": curr_user.id,
      "name": curr_user.name,
      "email": curr_user.email,
      "number": curr_user.number,
    }
  except Exception as e:
    print(e)
    return "Something went wrong"

@app.route("/login", methods=["POST"])
@cross_origin(origin='*')
def loginUser():
  user = request.get_json()
  curr_user = Users.query.where(Users.email == user["email"]).first()
  if curr_user.checkLoginCreds(email=user["email"], password=user["password"]):
    login_user(curr_user)
    return "User logged in"

  return "Username or password is incorrect"


@app.route("/create-user", methods=["POST"])
@cross_origin(origin='*')
def createUser():
  user = request.get_json()
  curr_user = Users.query.where(Users.email == user["email"]).first()
  if curr_user:
    response =  make_response("User already there")
    response.status = "406"
    return response
  new_user = Users(
    name=user["name"],
    email=user["email"],
    password=user["password"],
    number=user["number"]
  )
  try:
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    return "User Added"
  except Exception as e:
    print(e)
    return "Something went wrong"
    
@app.route('/logout')
@cross_origin(origin='*')
@login_required
def logout_page():
    logout_user()
    return "User Logged out"