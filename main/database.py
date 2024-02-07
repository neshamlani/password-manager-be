from sqlalchemy.orm import Mapped, mapped_column
from main import app,db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
  __tablename__ = "users"
  id:Mapped[int] = mapped_column(db.Integer, primary_key=True)
  name: Mapped[str] = mapped_column(db.String, nullable=False)
  email: Mapped[str] = mapped_column(db.String, nullable=False)
  password: Mapped[str] = mapped_column(db.String, nullable=False)
  number: Mapped[str] = mapped_column(db.String, nullable=False)

  def checkLoginCreds(self, email, password):
     return self.email == email and self.password == password


# Create the DB after all the db models are created
with app.app_context():
  db.create_all()