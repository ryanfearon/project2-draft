# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html")


    
# Using Postgres to load data
# POSTGRES = {
#     'user': 'postgres',
#     'pw': 'postgres',
#     'db': 'mentalhealth_db',
#     'port': '5432',
# }
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:delilahjones@localhost:5432/mentalhealth_db'
POSTGRES = {
    'user': 'postgres',
    'pw': 'delilahjones',
    'db': 'mentalhealth_db',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

if __name__ == "__main__":
    app.run(debug=True)