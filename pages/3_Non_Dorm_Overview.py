import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Non Dorm Overview",
    page_icon="👋",
)

annual_data = pd.read_csv('data/Non-Dorm Annual Basic Stats.csv', index_col='Stat Type')

def overall_change_year():
    data = annual_data.filter(regex='Total Energy')
    data = data.drop(data.index[0])
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.subheader('Total Energy Consumption by Building for Each Year in kBTU')
    st.bar_chart(data=data)

def average_total_building():
    data = annual_data.filter(regex='Total Energy')
    data = data.filter(regex='Mean ', axis=0)
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    fig = px.pie(values=data.iloc[0], names=data.columns)
    st.subheader('Average Total Energy Consumption by Building in kBTU')
    st.plotly_chart(fig)

def average_total_type():
    data = annual_data.filter(regex='Total Energy')
    

overall_change_year()
average_total_building()

