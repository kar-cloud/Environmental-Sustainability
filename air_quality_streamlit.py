import pandas as pd
import time
import requests
import streamlit as st

# Change the layout of the page to a huge width
st.set_page_config(page_title="Air Quality Monitoring", layout="wide")

FLASK_URL = "http://127.0.0.1:5000"

@st.cache_data
def get_dataframe_object():
    """
    - Function to return a dataframe object of the air quality data fetched from flask backend
    - It accepts no parameters
    - It returns a dataframe object
    """

    try:
        response = requests.get(f"{FLASK_URL}/data")

        if response and response.json():
            return pd.DataFrame(response.json())
    except Exception as e:
        return pd.DataFrame()

df = get_dataframe_object()

st.title("Air Quality Monitoring for New Delhi")

# ---------- Table Content ------------
st.subheader("Air Quality Pollutants Table")
date_range = st.date_input("Filter by Date", [])

filtered_df = df.copy()
if date_range and len(date_range) == 2:
    filtered_df = filtered_df[
        (pd.to_datetime(filtered_df["time"]).dt.date >= date_range[0]) & 
        (pd.to_datetime(filtered_df["time"]).dt.date <= date_range[1])
    ]
st.dataframe(filtered_df)

# ----------- Graphs Display ----------------
st.subheader("Pollutants Daily Concentration Graphs")

update_interval = st.slider("Update Interval (seconds)", min_value=0.2, max_value=2.0, value=0.2)
pollutants = ["pm2_5", "ozone", "nitrogen_dioxide", "sulphur_dioxide",
              "carbon_monoxide", "uv_index", "dust"]

df_date = df.copy()
df_date["date"] = pd.to_datetime(df["time"]).dt.date
df_24_hours = df_date.groupby("date")[pollutants].mean().reset_index()

real_time_data = pd.DataFrame(columns=["date"] + pollutants)
pollutant_graphs = {}

# Create an empty graph for all pollutants
for pollutant in pollutants:
    st.subheader(pollutant.upper())
    pollutant_graphs[pollutant] = st.empty()

# Real-time simulation: Iterate through the daily data DataFrame
for i in range(len(df_24_hours)):
    # Get the latest row of data
    row = df_24_hours.iloc[i]

    new_row = {"date": row["date"]}
    for pollutant in pollutants:
        new_row[pollutant] = row[pollutant]

    # Append the new row to the real-time DataFrame
    real_time_data = pd.concat([real_time_data, pd.DataFrame([new_row])])
    plot_data = real_time_data.set_index("date")

    # After each interval the line chart is created for all the pollutants making it
    # look like it is being updated in real-time
    for pollutant in pollutants:
        pollutant_graphs[pollutant].line_chart(plot_data[[pollutant]])

    # Simulate real-time by waiting for 1 second
    time.sleep(update_interval)