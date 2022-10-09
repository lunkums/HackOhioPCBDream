import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

st.write("# Welcome to OSU Campus Energy Dashboard! 💃")

st.sidebar.success("Select a dashboard above.")

df = pd.read_csv('data/Non-Dorm Annual Means per Person.csv', index_col='StatType')

# mean_rows = df.filter(regex="^Mean", axis=0)  # select rows
# mean_gas = mean_rows.filter(regex='Natural Gas Consumption', axis=1)  # select columns
# mean_electric = mean_rows.filter(regex='Electricity Consumption', axis=1)
# gasSum = mean_gas.to_numpy(na_value=0).flatten().sum()
# electricSum = mean_electric.to_numpy(na_value=0).flatten().sum()
# totalSum = gasSum + electricSum
# print(totalSum)
# print(gasSum)
# print(electricSum)
# gasP = gasSum/totalSum * 100
# elecP = electricSum/totalSum * 100
# #print(gasSum/totalSum *100)
# # df = pd.DataFrame({'mass': [0.330, 4.87 , 5.97],
# #                    'radius': [2439.7, 6051.8, 6378.1]},
# #                   index=['Mercury', 'Venus', 'Earth'])
# # plot = df.plot.pie(y='mass', figsize=(5, 5))
# # st.pyplot(plot.figure)
# cDF = pd.DataFrame({'Percents': [gasP, elecP]}, index = ['Natural Gas', 'Electric'])
# plot = cDF.plot.pie(y='Percents', figsize=(3,3), radius = 0.9)
# st.pyplot(plot.figure)

annual_data = pd.read_csv(
    'data/Non-Dorm Annual Basic Stats.csv', index_col='Stat Type')

#TODO need to include non-dorm and dorm data together!


def overall_change_year():
    data = annual_data.filter(regex='Total Energy')
    data = data.drop(data.index[0])
    for col in data.columns:
        data.rename(columns={col: col.replace(
            " - Total Energy Consumption (Cleaned) (kBTU)", "")}, inplace=True)

    building_names = data.columns

    all_options = st.checkbox("Select all buildings", value=True)

    if all_options:
        select_buildings = data.columns
    else:
        select_buildings = st.multiselect(
            "Select Buildings to Compare",
            building_names,
            default = building_names[0]
        )

    st.subheader('Total Energy Consumption by Building for Each Year in kBTU')
    st.bar_chart(data=data[select_buildings])


overall_change_year()


# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )
