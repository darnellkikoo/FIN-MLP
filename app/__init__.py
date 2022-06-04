from .components import prompt, home
import pickle as pkl
import streamlit as st

@st.cache
def load_model():
    with open("./resources/model.pickle", 'rb') as file:
        model = pkl.load(file)
    return model

def run_app():
    st.set_page_config(
        page_title='Flight Passenger Satisfaction',
        page_icon='✈️'
    )
    model = load_model()    
    df = prompt()
    home(df, model)