from PIL import Image
from ..utils import get_review, problem_details, satisfaction_details
import streamlit as st

table_columns = ['Inflight wifi service', 'Departure/Arrival time convenient',
    'Ease of Online booking', 'Gate location','Food and drink',
    'Online boarding','Seat comfort','Inflight entertainment',
    'On-board service','Leg room service','Baggage handling',
    'Checkin service', 'Inflight service', 'Cleanliness'
]

@st.cache
def get_image():
    return Image.open("./resources/flight.webp")

def display_header():
    st.title("Flight Passenger Satisfaction")
    st.subheader("COMP67450001 - Machine Learning Final Project")
    st.caption('2440009654 - Darnell Kikoo ⬥ 2440009162 - Matthew Adrianus Mulyono ⬥ 2440076450 - Winson Allan Wijaya')
    st.image(get_image())
    st.write(f'<div style="text-align:justify;">{problem_details}</div><br>', unsafe_allow_html=True)

def display_data(df):
    col1, col2 = st.columns(2)
    col1.metric("Passenger information", f"{int(df['Age'])} year old {str(df['Gender'])}")
    col2.metric("Customer type", str(df['Customer Type']).capitalize())
    f1, f2, f3 = st.columns([2,2,1])
    f1.metric("Flight type", str(df['Type of Travel']).capitalize())
    f2.metric("Flight class", f"{str(df['Class']).capitalize()} class")
    f3.metric("Flight distance (in km)", f"{int(df['Flight Distance'])}")  
    map_satisfaction = lambda x:satisfaction_details.get(str(x))
    for col in table_columns:
        df[col] = map_satisfaction(int(df[col]))
    cols = [[table_columns[0:4],table_columns[4:7]], [table_columns[7:10], table_columns[10:14]]]
    for col in cols:
        ss = st.columns([len(col[0]), len(col[1])])
        for s,c in zip(ss,col): 
            s.dataframe(df[c])
            
def display_statistics():
    reviews = get_review()
    z, r1, r2, r3, z1 = st.columns([1,2,2,2,1])
    yes, no = reviews.get('yes'), reviews.get('no')
    r1.metric("Right predictions", yes)
    r2.metric("Wrong predictions", no)
    accuracy = round((yes*100)/(yes+no),2) if yes+no!=0 else 100
    r3.metric("Accuracy", f"{accuracy}%")

