from flask import Flask

app = Flask(__name__)
__name__ = "__main__"
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite://C:/Users/jeffrey.moody/Source/Repos/FlaskWebProject1_Test/FlaskWebProject1_Test/database.db'
app.config['SQLALCHEMY_TRACKMODIFICATION'] = False
