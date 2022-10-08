import streamlit as st
import pandas as pd

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

st.write("# Welcome to OSU Campus Energy Dashboard! 💃")

st.sidebar.success("Select a dashboard above.")

df = pd.read_csv('data/Annual Means per Person.csv', index_col = 'StatType')



mean_rows = df.filter(regex="^Mean", axis=0)  # select rows
mean_gas = mean_rows.filter(regex='Natural Gas Consumption', axis=1)  # select columns
mean_electric = mean_rows.filter(regex='Electricity Consumption', axis=1)
gasSum = mean_gas.to_numpy(na_value=0).flatten().sum()
electricSum = mean_electric.to_numpy(na_value=0).flatten().sum()
totalSum = gasSum + electricSum
print(totalSum)
print(gasSum)
print(electricSum)
gasP = gasSum/totalSum * 100
elecP = electricSum/totalSum * 100
#print(gasSum/totalSum *100)
# df = pd.DataFrame({'mass': [0.330, 4.87 , 5.97],
#                    'radius': [2439.7, 6051.8, 6378.1]},
#                   index=['Mercury', 'Venus', 'Earth'])
# plot = df.plot.pie(y='mass', figsize=(5, 5))
# st.pyplot(plot.figure)
cDF = pd.DataFrame({'Percents': [gasP, elecP]}, index = ['Natural Gas', 'Electric'])
plot = cDF.plot.pie(y='Percents', figsize=(3,3), radius = 0.9)
st.pyplot(plot.figure)

#now compare percent of electric to gas annual means per person

#print(mean_electric.sum())
#plot = df.plot.pie(y='Energy consumed', figsize=(5, 5))
#print(mean_rows)#

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
