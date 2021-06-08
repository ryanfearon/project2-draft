# import necessary libraries

import pandas as pd
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

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
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Mental_health = Base.classes.mental_health

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/physical")
def physical():
    """Return a list of sample names."""

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])

@app.route("/metadata/<sample>")
def sample_metadata(sample):
    """Return the MetaData for a given sample."""
    sel = [
        Mental_health.year,
        Mental_health.physical_importance,
        Mental_health.mental_importance,
        Mental_health.industry_support,

    ]

    results = db.session.query(*sel).all()

    print(sample_metadata)
    return jsonify(sample_metadata)

if __name__ == "__main__":
    app.run(debug=True)