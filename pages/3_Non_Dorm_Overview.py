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
    st.line_chart(data=data)

def overall_change_year_type():
    data = annual_data.filter(regex='Total Energy')
    data = data.drop(data.index[0])
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.bar_chart(data=data)

def total_average_energy():
    data = annual_data.filter(regex='Total Energy')
    data = data.filter(regex='Mean', axis=0)
    data['Energy Consumption (kbTU)'] = data.filter(like='Total').sum(1)
    data = data[data.columns.drop(list(data.filter(regex='Total Energy')))]
    st.metric(label="Average Total Energy Consumption per Year (kbTU)", value=round(data['Energy Consumption (kbTU)'], 2))

def overall_change_year():
    data = annual_data.filter(regex='Total Energy')
    data = data.drop(data.index[0])
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.subheader('Total Energy Consumption by Building for Each Year in kBTU')
    st.line_chart(data=data)

def average_total_building():
    data = annual_data.filter(regex='Total Energy')
    data = data.filter(regex='Mean ', axis=0)
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    fig = px.pie(values=data.iloc[0], names=data.columns)
    st.subheader('Percentages of Average Total Energy Consumption by Building in kBTU')
    st.plotly_chart(fig)

def average_total_type():
    data = annual_data.filter(regex='Mean ', axis=0)
    data['Steam Consumption (kbTU)'] = data.filter(like='Steam').sum(1)
    data['Chilled Water Consumption (kbTU)'] = data.filter(like='Chilled').sum(1)
    data['Electricity Consumption (kbTU)'] = data.filter(like='Electricity').sum(1)
    data['Hot Water Consumption (kbTU)'] = data.filter(like='Hot').sum(1)
    data['Natural Gas Consumption (kbTU)'] = data.filter(like='Natural').sum(1)
    data = data[data.columns.drop(list(data.filter(regex=' - ')))]
    st.subheader('Percentages of Average Yearly Total Energy Consumption by Type')
    fig = px.pie(values=data.iloc[0], names=data.columns)
    st.plotly_chart(fig)



overall_change_year()
overall_change_year_type()
total_average_energy()
average_total_building()
average_total_type()

