import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Define a function to calculate the number of iPhones that could be purchased with 1 Bitcoin each year
def calculate_iphones_per_bitcoin(bitcoin_price, iphone_price):
    return bitcoin_price / iphone_price

# Initialize data
data = {
    'Year': [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'BitcoinPrice': [0.01, 0.09, 0.014, 0.30, 5.49, 13.30, 756, 315, 400, 1001, 13600, 3800, 8000, 29800, 47686.81],
}

df = pd.DataFrame(data)

iphone_price = 1000  # change this if the iPhone price changes

df['iPhonesPerBitcoin'] = df['BitcoinPrice'].apply(lambda x: calculate_iphones_per_bitcoin(x, iphone_price))

# Convert 'Year' column to string for table
df_table = df.copy()
df_table['Year'] = df_table['Year'].astype(str)

# Streamlit App
st.title("Bitcoin value in terms of iPhone over the years")

# Display the table
st.table(df_table)

# Plotting
fig = go.Figure()

# Adding traces
fig.add_trace(go.Bar(name='Bitcoin in USD', x=df['Year'], y=df['BitcoinPrice']))
fig.add_trace(go.Bar(name='iPhones per Bitcoin', x=df['Year'], y=df['iPhonesPerBitcoin']))
fig.add_trace(go.Scatter(name='Bitcoin Price Line', x=df['Year'], y=df['BitcoinPrice'], mode='lines'))
fig.add_trace(go.Scatter(name='iPhones per Bitcoin Line', x=df['Year'], y=df['iPhonesPerBitcoin'], mode='lines'))

# Update layout to use a logarithmic scale
fig.update_layout(
    barmode='group',
    yaxis_type="log"
)

st.plotly_chart(fig)

# Adding a scatter plot
fig2 = go.Figure()

fig2.add_trace(go.Scatter(name='Bitcoin Price Scatter', x=df['Year'], y=df['BitcoinPrice'], mode='markers'))
fig2.add_trace(go.Scatter(name='iPhones per Bitcoin Scatter', x=df['Year'], y=df['iPhonesPerBitcoin'], mode='markers'))

fig2.update_layout(
    yaxis_type="log"
)

st.title("Scatter plot view")
st.plotly_chart(fig2)

# Adding a line chart
st.title("Line chart view")
fig3 = px.line(df, x='Year', y=['BitcoinPrice', 'iPhonesPerBitcoin'], log_y=True)
st.plotly_chart(fig3)

# Adding an area chart
st.title("Area chart view")
fig4 = px.area(df, x='Year', y='iPhonesPerBitcoin', log_y=True)
st.plotly_chart(fig4)
