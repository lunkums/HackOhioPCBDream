import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit.components.v1 as components

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

st.write("# Welcome to OSU Campus Energy Dashboard! 💃")

df = pd.read_csv('data/Non-Dorm Annual Means per Person.csv',
                 index_col='StatType')

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

annual_Nondorm_data = pd.read_csv(
    'data/Non-Dorm Annual Basic Stats.csv', index_col='Stat Type')

annual_Dorm_data = pd.read_csv(
    'data/Dorm Annual Basic Stats.csv', index_col='Stat Type')

#TODO need to include non-dorm and dorm data together!
#print(combined_data)

#HtmlFile = open("EnergyVisualizationBuild\index.html", 'r', encoding='utf-8')
#source_code = HtmlFile.read() 
#print(source_code)
components.iframe("https://lunkums.github.io/EnergyVisualizationTool/", height=750, width=1250)


def combine_all_buildings():
    left = annual_Dorm_data.filter(regex='Total Energy', axis=1)
    left = left.drop(['Mean (2017-2022)'])
    #st.dataframe(left)
    right = annual_Nondorm_data.filter(regex='Total Energy', axis=1)
    right = right.drop(['Mean (2017-2022)'])
    #st.dataframe(right)

    data = left.merge(right, left_index=True, right_index=True, how='inner')
    #st.dataframe(data)

    for col in data.columns:
        data.rename(columns={col: col.replace(
            " - Total Energy Consumption (Cleaned) (kBTU)", "")}, inplace=True)

    return data


def combined_change_year():
    data = combine_all_buildings()
    st.dataframe(data)
    building_names = data.columns
    all_years_list = list(data.index)
    #st.sidebar.write("Barchart Filter")
    #form = st.form(key='bcf')
    
    with st.sidebar:
        with st.expander("Barchart Filter"):
            c = st.container()   
            all_options = c.checkbox("Select all buildings", value=True)
            if all_options:
                select_buildings = data.columns
                st.snow()
            else:
                select_buildings = c.multiselect(
                    "Select Buildings to Compare",
                    building_names,
                    default=building_names[0]
                )
            

            all_years = c.checkbox("Select Years", value=True)
            select_years = all_years_list
            if not all_years:
                select_years = c.multiselect(
                    "Select Buildings to Compare",
                    select_years,
                    default=select_years[0]
                )


    st.subheader('Total Energy Consumption by Building for Each Year in kBTU')
    st.bar_chart(data=data.loc[select_years, select_buildings])


def combined_average_total_building():
    data = pd.concat([annual_Nondorm_data, annual_Dorm_data],
                     axis=0, ignore_index=False)
    data = data.filter(regex='^Mean\s\D\d*\D\d*$', axis=0)
    data = data.filter(regex='Total Energy')

    data = combine_all_buildings()

    fig = px.pie(values=data.iloc[0], names=data.columns)
    st.subheader('Average Total Energy Consumption by Building in kBTU')
    st.plotly_chart(fig)


combined_change_year()
combined_average_total_building()


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
