from flask import Flask
import pandas as pd
import json
import os
from flask_sqlalchemy import SQLAlchemy

# Fetch the environment variables for SQL.
host = os.getenv("SQL_HOST")
user = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")
port = os.getenv("SQL_PORT")

app = Flask(__name__)

# Create SQL connection
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{user}:Karan%40123@{host}:{port}/air_quality_monitoring_db"
app.config["SECRET_KEY"] = "secret_key"
db = SQLAlchemy(app)

@app.route("/data", methods=["GET"])
def get_data():
    """
    - "/data" route will fetch all the data from the SQL server and return to the user in JSON format
    """
    
    df = pd.read_sql("SELECT * FROM air_quality_transformed", con=db.engine)
    df["time"] = df["time"].astype(str)
    return json.dumps(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
