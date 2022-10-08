import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Non Dorm Overview",
    page_icon="👋",
)

annual_data = pd.read_csv('data/Non-Dorm Annual Basic Stats.csv')


