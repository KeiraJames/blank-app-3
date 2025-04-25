import streamlit as st

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
