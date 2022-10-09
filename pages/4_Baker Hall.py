import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

st.set_page_config(
    page_title="Baker Hall",
    page_icon="👋",
)

st.title("Baker Halls Energy Consumption Dashboard")

annual_basic = pd.read_csv('data/Dorm Annual Basic Stats.csv', index_col='Stat Type')
monthly_basic = pd.read_csv('data/Dorm Monthly YTD.csv', index_col='Series Name')
monthly_person = pd.read_csv('data/Dorm Monthly YTD per Person.csv', index_col='Series Name')

image = Image.open('images/baker-hall.jpg')

def dorm_champ():
    data = monthly_basic.filter(regex='Total Energy')
    data = data.filter(regex="9-Sep", axis=0)
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    data = data.swapaxes("index", "columns")
    data = data.rename(columns={"9-Sep": 'Total Energy Consumption (kBTY)'})
    data = data.sort_values(by=['Total Energy Consumption (kBTY)'])
    li = data.index.tolist()
    st.metric(label="September Champion of Energy Savings", value=li[0])

def dorm_ranking():
    data = monthly_basic.filter(regex='Total Energy')
    data = data.filter(regex="9-Sep", axis=0)
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    data = data.swapaxes("index", "columns")
    data = data.rename(columns={"9-Sep": 'Total Energy Consumption (kBTY)'})
    data = data.sort_values(by=['Total Energy Consumption (kBTY)'])
    data.insert(0, 'Rank', range(1, 1 + len(data)))
    i = data.index.get_loc('Baker Hall')
    st.metric(label="September 2022 Ranking in Least Energy Consumption", value='#' + str(round(data.iloc[i][0])))

def overall_change_month():
    data = monthly_basic.filter(regex='Total Energy')
    data = data.filter(regex='Baker Hall')
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.markdown('Total Energy Consumption for Each Month YTD (2022) in kBTU')
    st.line_chart(data=data)

def overall_change_year():
    data = annual_basic.filter(regex='Total Energy')
    data = data.filter(regex='Baker Hall')
    data = data.drop(data.index[0])
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.markdown('Total Energy Consumption for Each Year in kBTU')
    st.line_chart(data=data)

def average_total_type():
    data = annual_basic.filter(regex='Mean ', axis=0)
    data = data.filter(regex='Baker Hall')
    data['Steam Consumption (kbTU)'] = data.filter(like='Steam').sum(1)
    data['Chilled Water Consumption (kbTU)'] = data.filter(like='Chilled').sum(1)
    data['Electricity Consumption (kbTU)'] = data.filter(like='Electricity').sum(1)
    data['Hot Water Consumption (kbTU)'] = data.filter(like='Hot').sum(1)
    data['Natural Gas Consumption (kbTU)'] = data.filter(like='Natural').sum(1)
    data = data[data.columns.drop(list(data.filter(regex=' - ')))]
    st.markdown('Percentages of Average Yearly Total Energy Consumption by Type')
    fig = px.pie(values=data.iloc[0], names=data.columns)
    st.plotly_chart(fig)

def overall_change_month_person():
    data = monthly_person.filter(regex='Total Energy')
    data = data.filter(regex='Baker Hall')
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.markdown('Total Energy Consumption per Person for Each Month YTD (2022) in kBTU')
    st.line_chart(data=data)

col1, col2 = st.columns([3,2])

with col1:
    st.image(image)
with col2:
    dorm_ranking()

col3, col4 = st.columns(2)

with col3:
    overall_change_month()
with col4:
    overall_change_month_person()

col5, col6 = st.columns(2)

with col5:
    overall_change_year()
with col6:
    average_total_type()


