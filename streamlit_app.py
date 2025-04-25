import streamlit as st
import time
from pymongo import MongoClient
uri = "mongodb+srv://recent:recent@cluster0.i7fqn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client['temp_moisture'] 
collection = db['c1']  


def get_latest_stats():
    latest_data = collection.find().sort('timestamp', -1).limit(1)  # Sort by timestamp descending
    return latest_data[0] if latest_data.count() > 0 else None

st.title("Plant Care Monitor")

# Button to fetch the latest data
if st.button("Give Me Stats Update"):
    data = get_latest_stats()

    if data:
        temperature = data["temperature"]
        moisture_value = data["moisture_value"]
        timestamp = data["timestamp"]

        st.write(f"**Temperature**: {temperature}°C")
        st.write(f"**Moisture Level**: {moisture_value}")
        st.write(f"**Last Updated**: {timestamp}")

        if moisture_value < 300:  # Example threshold for moisture
            st.warning("Your plant needs water!")
        elif moisture_value < 600:
            st.info("Your plant is doing okay!")
        else:
            st.success("Your plant is happy and hydrated!")
    else:
        st.error("No data available.")
