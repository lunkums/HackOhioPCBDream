import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(
    page_title="Non Dorm Overview",
    page_icon="👋",
)

annual_data = pd.read_csv('data/Non-Dorm Annual Basic Stats.csv')

def overall_change_year():
    data = annual_data[annual_data["Stat Type"].str.contains("Standard Deviation")==False]
    data = data.set_index('Stat Type')
    data = data.filter(regex='Total Energy')
    data = data.drop(data.index[0])
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.subheader('Total Energy Consumption by Building for Each Year')
    st.bar_chart(data=data)

overall_change_year()

