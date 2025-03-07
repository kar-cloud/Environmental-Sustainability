# Data-Driven Sustainability: Tracking Air for a Greener Future

## Pre-requisities
The project requires some pre-requisites for working:
- Windows Platform
- Python 3.12.5
- MySQL
- VSCode or Jupyter IDE

## Introduction
The following project is for tracking air quality under environmental sustainability
- The section first fetches data from the Open Meteo API for air quality in New Delhi in JSON format. 
- The collected JSON data is converted to CSV format and initially saved in a MySQL Database.
- Data is transformed and cleaned using various techniques and further visualizations have been done to analyze the patterns in the data
- Machine learning models (Random Forest and Decision Tree) have been created for prediction of harmful PM2.5 levels in the air.
- Finally the cleaned data is stored into the MySQL Database.
- The goal of the project is to understand the major cause of bad air quality and get insights on how pollutants such as
Carbon Monoxide, PM2.5, Ozone etc. affects air quality.

## API Source
https://open-meteo.com/en/docs/air-quality-api

## Project Directory
The following project directory contains following files:
- **air_quality.ipynb** - This jupyter file consists code for transformation and visualization for the dataset
- **air_quality_flask.ipynb** - This python file consists backend code for the Flask application
- **air_quality_streamlit.ipynb** - This python file consists code for streamlit to stream data on the web
- **air_quality.csv** - CSV file which is generated after fetching data from the API
- **air_quality_transformed.csv** - Cleaned and Transformed version of air quality CSV file  
- **README.md** - Description file for the whole project

## Setting up of Virtual Environment
After downloading the zip file, the following steps are to be followed for creating a virtual environment for the project:
1. In your terminal, move to the project directory using `cd` command
2. Run the command to create a python virtual environment: `python -m venv venv`
3. Run the command to activate the virtual environment: `venv\Scripts\activate`

## Installing the required dependencies
The following project requires some libraries to be installed. Following command needs to be run
for smooth operations of the project: `pip install requests mysql-connector-python pandas seaborn matplotlib numpy scikit-learn Flask Flask-SQLAlchemy streamlit`

## Creating Environment Variables
The air section requires some environment variables to be set. 
Following commands need to be run in terminal for running the problem 1: `setx MYSQL_HOST <mysql_host>`, `setx MYSQL_USERNAME <mysql_username>`, `setx MYSQL_PASSWORD <mysql_password>`, `setx MYSQL_PORT <mysql_port>`.
NOTE: Once you set the environment variables, you would have to close the terminal or restart the device to get the change reflected.

## Running the code
- There is a jupyter files: `air_quality.ipynb` which should be run in sequential manner for correct flow of the data. 
- For running the web application, backend flask service needs to be turned on using command: `python air_quality_flask.py` which can be tested
further on `http://127.0.0.1:5000/`.
- For running the streamlit application, following command should be run: `streamlit run air_quality_streamlit.py`
