from pandas import DataFrame
from ..utils import case_details, help_details
import streamlit as st

def prompt():
    # Customer Information
    st.sidebar.markdown("### Insert passenger information")
    gender = st.sidebar.selectbox("Gender", options=["Male","Female"], help = help_details.get('gender'))
    age = st.sidebar.number_input("Age", min_value=0, max_value=125, value=30, help=help_details.get('age'))
    # Flight Information
    st.sidebar.markdown("### Insert flight information")
    customer_type = st.sidebar.selectbox("Customer Type", options=["Loyal Customer", "Disloyal Customer"], help = help_details.get('customer_type'))
    travel_type = st.sidebar.selectbox("Flight Type", options=['Business Travel', 'Personal Travel'], help=help_details.get('travel_type'))
    travel_class = st.sidebar.selectbox("Flight Class", options=['Eco', 'Eco Plus', 'Business'], help=help_details.get('travel_class'))
    distance = st.sidebar.number_input("Flight Distance (in km)", min_value=5, max_value = 10000, value = 2500, help=help_details.get('distance'))
    # Service satisfaction (0-5) -> Slider
    st.sidebar.markdown("### Rate your satisfaction level")
    wifi = st.sidebar.slider("Inflight Wifi Service", min_value=0, max_value=5, value=3, help=help_details.get('wifi'))
    dep_arr = st.sidebar.slider("Departure/Arrival Time", min_value=0, max_value=5, value=3, help=help_details.get('dep_arr'))
    booking = st.sidebar.slider("Ease of Online Booking", min_value=0, max_value=5, value=3, help=help_details.get('booking'))
    gate = st.sidebar.slider("Gate Location", min_value=0, max_value=5, value=3, help=help_details.get('gate'))
    fnb = st.sidebar.slider("Food and Drinks", min_value=0, max_value=5, value=3, help=help_details.get('fnb'))
    online_boarding = st.sidebar.slider("Online Boarding", min_value=0, max_value=5, value=3, help=help_details.get('online_boarding'))
    seat = st.sidebar.slider("Seat Comfort", min_value=0, max_value=5, value=3, help=help_details.get('seat'))
    entertainment = st.sidebar.slider("Inflight Entertainment", min_value=0, max_value=5, value=3, help=help_details.get('entertainment'))
    onboard_service = st.sidebar.slider("On-board Service", min_value=0, max_value=5, value=3, help=help_details.get('onboard_service'))
    leg = st.sidebar.slider("Leg Room Service", min_value=0, max_value=5, value=3, help=help_details.get('leg'))
    baggage = st.sidebar.slider("Baggage Handling", min_value=0, max_value=5, value=3, help=help_details.get('baggage'))
    check_in = st.sidebar.slider("Check-in Service", min_value=0, max_value=5, value=3, help=help_details.get('checkin'))
    service = st.sidebar.slider("Inflight services", min_value=0, max_value=5, value=3, help=help_details.get('service'))
    clean = st.sidebar.slider("Cleanliness", min_value=0, max_value=5, value=3, help=help_details.get('clean'))
    # Delays
    st.sidebar.markdown("### Are there any delays?")
    dep_delay = st.sidebar.number_input("Departure Delay in minutes", min_value = 0, help=help_details.get('dep_delay'))
    arr_delay = st.sidebar.number_input("Arrival Delay in minutes", min_value = 0, help=help_details.get('arr_delay'))

    return DataFrame({
        'Gender':[gender, 'Male' if gender == 'Female' else 'Female'],
        'Customer Type':case_details.get('customer_type').get(customer_type),
        'Age':age,
        'Type of Travel':[case_details.get('travel_type').get(travel_type), 'Business travel' if travel_type == 'Personal Travel' else 'Personal Travel'],
        'Class':travel_class,
        'Flight Distance':distance,
        'Inflight wifi service': wifi,          
        'Departure/Arrival time convenient':dep_arr,
        'Ease of Online booking':booking,
        'Gate location':gate,
        'Food and drink': fnb,
        'Online boarding':online_boarding,
        'Seat comfort':seat,
        'Inflight entertainment':entertainment,
        'On-board service':onboard_service,
        'Leg room service':leg,
        'Baggage handling':baggage,
        'Checkin service':check_in,
        'Inflight service':service,
        'Cleanliness':clean,
        'Departure Delay in Minutes': dep_delay,
        'Arrival Delay in Minutes':arr_delay
    })

