from time import sleep
from ..components import display_header, display_data, display_statistics
from ..utils import add_review, preprocess_data
import streamlit as st

@st.cache
def predict_satisfaction(df, model):
    df = preprocess_data(df)
    return bool(model.predict(df))

def home(df, model):
    display_header()
    display_data(df.iloc[0])
    display_statistics()
    c1, c2, c3 = st.columns([2,2,1])
    if c3.button("Predict"):
        progress_container = st.empty()
        progress_bar = progress_container.progress(0)
        for i in range(100):
            sleep(0.01)
            progress_bar.progress(i+1)
        progress_container.empty()
        result = predict_satisfaction(df, model)
        if result:
            st.success("Customer is satisfied!!")
        else:
            st.error("Customer is unsatisfied!")
        st.write("Are you satisfied with our prediction?")
        a, s1, s2, s3, a1 = st.columns([2,1,1,1,2])
        s1.button("Yes", on_click=add_review, kwargs={'result':True})
        s2.button("No", on_click=add_review, kwargs={'result':False})
        s3.button("No Idea")
        