import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Non Dorm Overview",
    page_icon="👋",
)

st.title("Non-Dorm Overview Energy Consumption Dashboard")

annual_basic = pd.read_csv('data/Non-Dorm Annual Basic Stats.csv', index_col='Stat Type')
annual_person = pd.read_csv('data/Non-Dorm Annual Means per Person.csv', index_col='StatType')
monthly_basic = pd.read_csv('data/Non-Dorm_Monthly_YTD.csv', index_col='Stat Type')
monthly_person = pd.read_csv('data/Non-Dorm_Monthly_YTD per Person.csv', index_col='Stat Type')


def overall_change_year():
    data = annual_basic.filter(regex='Total Energy')
    data = data.drop(data.index[0])
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.markdown('Total Energy Consumption by Building for Each Year in kBTU')
    st.line_chart(data=data)

def overall_change_year_type():
    data = annual_basic.filter(regex='Total Energy')
    data = data.drop(data.index[0])
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.markdown('Total Energy Consumption by Building for Each Year in kBTU')
    st.bar_chart(data=data)

def total_average_energy():
    data = annual_basic.filter(regex='Total Energy')
    data = data.filter(regex='Mean', axis=0)
    data['Energy Consumption (kbTU)'] = data.filter(like='Total').sum(1)
    data = data[data.columns.drop(list(data.filter(regex='Total Energy')))]
    st.metric(label="Average Total Energy Consumption per Year (kbTU)", value=round(data['Energy Consumption (kbTU)'], 2))

def overall_change_year():
    data = annual_basic.filter(regex='Total Energy')
    data = data.drop(data.index[0])
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.markdown('Total Energy Consumption by Building for Each Year in kBTU')
    st.line_chart(data=data)

def average_total_building():
    data = annual_basic.filter(regex='Total Energy')
    data = data.filter(regex='Mean ', axis=0)
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    fig = px.pie(values=data.iloc[0], names=data.columns)
    st.markdown('Percentages of Average Total Energy Consumption by Building in kBTU')
    st.plotly_chart(fig)

def average_total_type():
    data = annual_basic.filter(regex='Mean ', axis=0)
    data['Steam Consumption (kbTU)'] = data.filter(like='Steam').sum(1)
    data['Chilled Water Consumption (kbTU)'] = data.filter(like='Chilled').sum(1)
    data['Electricity Consumption (kbTU)'] = data.filter(like='Electricity').sum(1)
    data['Hot Water Consumption (kbTU)'] = data.filter(like='Hot').sum(1)
    data['Natural Gas Consumption (kbTU)'] = data.filter(like='Natural').sum(1)
    data = data[data.columns.drop(list(data.filter(regex=' - ')))]
    st.markdown('Percentages of Average Yearly Total Energy Consumption by Type')
    fig = px.pie(values=data.iloc[0], names=data.columns)
    st.plotly_chart(fig)

def overall_change_year_person():
    data = annual_person.filter(regex='Total Energy') 
    data = data.drop(data.index[0])
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.markdown('Total Energy Consumption per Person by Building for Each Year in kBTU')
    st.line_chart(data=data)

def overall_change_year_type_person():
    data = annual_person.filter(regex='Total Energy')
    data = data.drop(data.index[0])
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.markdown('Total Energy Consumption per Person by Building for Each Year in kBTU')
    st.bar_chart(data=data)

def total_average_energy_person():
    data = annual_person.filter(regex='Total Energy')
    data = data.filter(regex='Mean', axis=0)
    data['Energy Consumption (kbTU)'] = data.filter(like='Total').sum(1)
    data = data[data.columns.drop(list(data.filter(regex='Total Energy')))]
    st.metric(label="Average Total Energy Consumption per Person per Year (kbTU)", value=round(data['Energy Consumption (kbTU)'], 2))

def average_total_building_person():
    data = annual_person.filter(regex='Total Energy')
    data = data.filter(regex='Mean ', axis=0)
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    fig = px.pie(values=data.iloc[0], names=data.columns)
    st.markdown('Percentages of Average Total Energy Consumption per Person by Building in kBTU')
    st.plotly_chart(fig)

def overall_change_month():
    data = monthly_basic.filter(regex='Total Energy')
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.markdown('Total Energy Consumption by Building for Each Month YTD (2022) in kBTU')
    st.line_chart(data=data)

def overall_change_month_person():
    data = monthly_person.filter(regex='Total Energy')
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.markdown('Total Energy Consumption per Person by Building for Each Month YTD (2022) in kBTU')
    st.line_chart(data=data)

col1, col2 = st.columns(2)

with col1:
    overall_change_month()
with col2:
    overall_change_month_person()

overall_change_year_type()

col3, col4 = st.columns([2, 4])
with col3:
    total_average_energy()
with col4:
    overall_change_year()

col5, col6 = st.columns([4, 2])
with col5:
    overall_change_year_person()
with col6:
    total_average_energy_person()

col7, col8 = st.columns(2)
with col7:
    average_total_building()
with col8:
    average_total_type()

col9, col10 = st.columns(2)
with col9:
    average_total_building_person()
with col10:
    overall_change_year_type_person()