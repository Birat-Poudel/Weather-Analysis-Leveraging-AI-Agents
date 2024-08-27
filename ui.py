import streamlit as st
from streamlit_autorefresh import st_autorefresh
from crews import Crews

crew = Crews()
    
st.title("Weather Analysis Leveraging AI Agents")

def get_weather_data(city_1, city_2, city_3):
    return crew.research_analysis_crew().kickoff(inputs={'cities': [city_1, city_2, city_3]})


city_1 = st.text_input("Enter the first city")
city_2 = st.text_input("Enter the second city")
city_3 = st.text_input("Enter the third city")

if st.button("Get Weather Data and Analyze"):
    with st.spinner("Gathering and Analyzing weather data..."):
        data = get_weather_data(city_1, city_2, city_3)
        
    st.subheader("Weather Data Analysis")
    st.markdown(data)

st_autorefresh(interval=5 * 60 * 1000)