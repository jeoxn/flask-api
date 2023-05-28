from flask import Flask
from Model  import db, DB_NAME


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from routes import routes

app.register_blueprint(routes)


with app.app_context():
    db.init_app(app)
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)