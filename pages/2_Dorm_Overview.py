import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Dorm Overview",
    page_icon="👋",
)

st.title("Dorm Overview Energy Consumption Dashboard")

annual_basic = pd.read_csv('data/Dorm Annual Basic Stats.csv', index_col='Stat Type')
monthly_basic = pd.read_csv('data/Dorm Monthly YTD.csv', index_col='Series Name')

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
    st.metric(label="September 2022 Champion of Energy Savings", value=li[0])

def dorm_ranking():
    data = monthly_basic.filter(regex='Total Energy')
    data = data.filter(regex="9-Sep", axis=0)
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    data = data.swapaxes("index", "columns")
    data = data.rename(columns={"9-Sep": 'Total Energy Consumption (kBTY)'})
    data = data.sort_values(by=['Total Energy Consumption (kBTY)'])
    data.insert(0, 'Rank', range(1, 1 + len(data)))
    st.markdown('Dorm Ranking in Least Total Energy Consumption - September 2022')
    st.table(data=data)

def overall_change_month():
    data = monthly_basic.filter(regex='Total Energy')
    for col in data.columns:
        data.rename(columns={col:col.replace(" - Total Energy Consumption (Cleaned) (kBTU)","")},inplace=True)
    st.markdown('Total Energy Consumption by Dorm for Each Month YTD (2022) in kBTU')
    st.line_chart(data=data)


col1, col2 = st.columns([3,2])

with col1:
    st.image(image, caption='Congratulations!')
with col2:
    dorm_champ()
    
dorm_ranking()
overall_change_month()