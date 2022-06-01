from pandas import DataFrame
from preprocessing import preprocess_data
import pickle as pkl
import streamlit as st
import time

with open("./resources/model.pickle", 'rb') as file:
    model = pkl.load(file)

st.title("Mau deploy jadi web katanya")

with st.sidebar:
    # Categories
    gender = st.selectbox("What's your gender?", options=["Male", "Female"])
    customer_type = st.selectbox("Are you a loyal customer of the flight service?", options=["Loyal Customer", "disloyal Customer"])
    travel_type = st.selectbox("What's the purpose of your flight?", options=['Business travel', 'Personal Travel'])
    travel_class = st.selectbox("What flight class are you in?", options=['Business', 'Eco Plus', 'Eco'])
    # Number input
    age = st.number_input("What's your age?", min_value=0, max_value=125)
    flight_distance = st.number_input("What's the how far is your destination (in km)", min_value=5)
    # Service satisfaction (0-5) -> Slider
    wifi = st.slider("How satisfied are you about the Inflight Wifi Service?", min_value=0, max_value=5)
    dep_arr = st.slider("How satisfied are you about the Departure/Arrival Time?", min_value=0, max_value=5)
    online_book = st.slider("How easy is it to book this flight online?", min_value=0, max_value=5)
    gate_loc = st.slider("How satisfied are you about the gate location?", min_value=0, max_value=5)
    fnb = st.slider("How satisfied are you with the Food and Drinks?", min_value=0, max_value=5)
    online_boarding = st.slider("How satisfied are you about the Online Boarding process?", min_value=0, max_value=5)
    seat_comfort = st.slider("How comfortable are your seats?", min_value=0, max_value=5)
    entertainment = st.slider("How satisfied are you about our entertainment system?", min_value=0, max_value=5)
    onboard_service = st.slider("How satisfied are you about the Onboard Service?", min_value=0, max_value=5)
    leg_room = st.slider("How comfortable is the leg room?", min_value=0, max_value=5)
    baggage_handling = st.slider("How satisfied are you on our baggage handling?", min_value=0, max_value=5)
    check_in = st.slider("How satisfied are you for our Checkin Service?", min_value=0, max_value=5)
    service = st.slider("How satisfied are you about our inflight services?", min_value=0, max_value=5)
    cleanliness = st.slider("Rate our cleanliness!!", min_value=0, max_value=5)
    # Delays
    dep_delay = st.number_input("Departure Delay in minutes", min_value = 0)
    arr_delay = st.number_input("Arrival Delay in minutes", min_value = 0)

df = DataFrame([{
    'Gender':gender,
    'Customer Type':customer_type,
    'Age':age,
    'Type of Travel':travel_type,
    'Class':travel_class,
    'Flight Distance':flight_distance,
    'Inflight wifi service': wifi,
    'Departure/Arrival time convenient':dep_arr,
    'Ease of Online booking':online_book,
    'Gate location':gate_loc,
    'Food and drink': fnb,
    'Online boarding':online_boarding,
    'Seat comfort':seat_comfort,
    'Inflight entertainment':entertainment,
    'On-board service':onboard_service,
    'Leg room service':leg_room,
    'Baggage handling':baggage_handling,
    'Checkin service':check_in,
    'Inflight service':service,
    'Cleanliness':cleanliness,
    'Departure Delay in Minutes': dep_delay,
    'Arrival Delay in Minutes':arr_delay
}])

st.dataframe(df)
if st.button("Predict"):
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i+1)
    df = preprocess_data(df)
    st.dataframe(df)
    # result = model.predict(df)
    # st.success(result)
